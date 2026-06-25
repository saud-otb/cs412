# File: ai.py
# Author: Saud Alotaibi
# Description: Helper that summarizes a game's reviews using the Gemini REST API.

import json
import urllib.request

from django.conf import settings

# Gemini REST endpoint. Using urllib (standard library) instead of the
# google-genai SDK so this works on any Python version with nothing to install.
GEMINI_API_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "gemini-2.5-flash:generateContent"
)


def summarize_reviews(game, reviews):
    '''Return an AI-generated overview of the given reviews for a game.

    Returns an empty string if there are no reviews. Raises on API errors so
    the caller can decide how to handle failures.'''

    if not reviews:
        return ""

    # Build the list of formatted review lines to include in the prompt
    lines = []
    for review in reviews:
        recommended = "Recommended" if review.recommended else "Not recommended"
        lines.append(
            f"- Rating {review.rating}/10 ({recommended}): "
            f"{review.review_title} - {review.review_text}"
        )

    # Compute the average rating to prepend to the AI response
    total = 0
    for review in reviews:
        total += review.rating

    average_rating = total / len(reviews)

    # Build the prompt instructing Gemini to summarize based only on the reviews
    prompt = (
        f"You are summarizing player reviews for the video game '{game.title}'.\n"
        f"Write a short overview (3-5 sentences), then a 'The Good' bullet list and a "
        f"'The Bad' bullet list, based ONLY on the reviews below. Do not invent details.\n\n"
        f"Reviews:\n" + "\n".join(lines)
    )

    # Send the prompt to the Gemini REST API as a JSON POST request
    body = json.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode("utf-8")
    request = urllib.request.Request(
        f"{GEMINI_API_URL}?key={settings.GEMINI_API_KEY}",
        data=body,
        headers={"Content-Type": "application/json"},
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        data = json.loads(response.read().decode("utf-8"))

    # Pull the generated text out of the API response
    text = data["candidates"][0]["content"]["parts"][0]["text"]

    return f"Average Rating: {average_rating:.1f}/10\n\n" + text
