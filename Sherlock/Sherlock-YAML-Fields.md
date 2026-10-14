# Sherlock YAML fields

## Challenge

| Field | Type | Description |
| --- | --- | --- |
| `scenario` | String | The story the player reads before investigating. Give the starting context and objective. Do not reveal attack techniques, answers, or the outcome. |
| `description` | String | A summary of what happens in the Sherlock, including techniques, investigation, and outcome. Spoilers are allowed here. |
| `difficulty` | String | Choose `Very Easy`, `Easy`, `Medium`, `Hard`, or `Insane`. |
| `author` | String | Sherlock creator(s). Separate multiple names with commas. |
| `prepared_by` | String | Writeup author(s). May be the same people as `author`. |
| `artifacts` | List | Evidence files supplied with the Sherlock. |
| `questions` | List | Questions the player answers. |

## Artifacts

Each entry in `artifacts` contains these fields.

| Field | Type | Description |
| --- | --- | --- |
| `name` | String | Filename, including its extension. |
| `hash` | String | Digest computed from the supplied file. Must match the selected algorithm. |
| `type` | String | Hash algorithm: `MD5`, `SHA-1`, `SHA-256`, or `SHA-512`. |

## Questions

Each entry in `questions` contains these fields.

| Field | Type | Description |
| --- | --- | --- |
| `number` | Integer | Unique positive question number. Start at `1` and number sequentially. |
| `title` | String | Question text. Specify the expected units, timezone, or format when needed. |
| `type` | String | Always use `task`. |
| `flag` | String | Expected answer. Quote numbers, timestamps, and boolean-looking answers. |
| `is_answer_case_sensitive` | Boolean | Default `false`. Choose `true` when capitalization must match exactly. |
| `is_optional` | Boolean | Always use `false`. |
| `version` | Integer | Always use `0`. |
| `requires` | Integer or null | Default `null`: visible from the start. Set an existing earlier question number to hide this question until that question is answered. |
| `placeholder` | String | Nonempty answer format guide or mask, such as `IPv4 address`, `YYYY-MM-DD hh:mm:ss`, or `'********'`. Custom text is supported. |
| `hint` | String | Optional clue. Omit it when no hint is needed. |

For example, `requires: 1` keeps a question hidden until question 1 is answered. Leave it as `null` unless this progression is intentional.
