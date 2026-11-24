# The Funniest Out-of-Office

[![make.fun](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/alvenze/funniest-out-of-office/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/alvenze/funniest-out-of-office/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)

One funny single-line out-of-office auto-reply, for the
[The Funniest Out-of-Office](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
bounty on make.fun. The program writes the reply to `/output/entry.txt`; an AI
judge compares entries two at a time through private blind rounds.

## The reply

> I'm out of office until Monday. I read your email the second it arrived. I'll reply on Monday as if I hadn't.

110 characters, one line. It keeps the shape of a real out-of-office reply a
person would actually set (away until Monday, reply on Monday), then confesses
the one thing every sender does and no auto-reply admits: he already read the
email the second it arrived. The closing beat, "as if I hadn't", turns the
Monday reply into a small shared fiction between sender and reader.

## How it works

`main.py` holds the reply as a fixed string and writes it to `/output/entry.txt`
(`OUTPUT_DIR` env var overrides the output directory, default `/output`). Before
writing, it runs the bounty gate on the text itself: 1-140 characters, not only
white space, a single line, valid UTF-8. The text is fixed, so both runs produce
byte-identical output.

## Run

```sh
python3 main.py
```

Writes `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt`).

## License

MIT, see `LICENSE`.
