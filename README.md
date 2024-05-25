# IPA-CHART

Simple [cloudflare worker](https://workers.cloudflare.com/) that returns the IPA characters and their sounds.

## ENDPOINTS

- `GET /char/vowels` : Returns the vowels.
- `GET /char/consonants` : Returns the consonants.
- `GET /char/others` : Returns others.
- `GET /char/name/:name` : Returns the characters of the name (e.g. `GET /char/name/Close front`).

## RESPONSE

```json
[
	{
		"id":1,
		"name":"Close front unrounded vowel",
		"symbol":"i",
		"audio":"https://www.ipachart.com/ogg/Close_front_unrounded_vowel.ogg",
		"audio_github":null,
		"type":"vowels"
	}
]

```
