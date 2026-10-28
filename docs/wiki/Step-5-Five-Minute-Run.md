# Step 5: the five-minute run

🌐 **English** · [Dansk](Step-5-Five-Minute-Run-da) · [Bahasa Melayu](Step-5-Five-Minute-Run-ms)

`run_bot` plays for 300 seconds in one loop: a burst of 20 clicks, then every second one visit to the store: upgrade crates first, then at most one product. At the end `get_cps` reads the cookies per second. The run in the screenshot reached **29 cookies per second** with 29 cursors, 17 grandmas and 2 upgrades (the first release reached 16.6).

**Screenshot**

![Step 5: the five-minute run](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory/raw/branch/main/docs/images/step-5-result.png)

**Function**

```python
while now - start < duration_seconds:
    click_cookie(game, CLICKS_PER_BURST)
    now = clock.monotonic()
    if now >= next_store_check:
        _buy_while_affordable(game)
        next_store_check = now + STORE_CHECK_INTERVAL_SECONDS
```

## What we gained

- **One loop, no threads.** The earlier solution used two threads and an extra package. One loop is easier to read, needs no extra dependency and is easy to test.
- **Inject the clock.** `run_bot` receives a `Clock`, so a fake clock tests a 300 second run in milliseconds.
- **Run the GUI in Docker.** Headless Chromium in a container never takes your mouse or keyboard, and the screenshots and the log come out as files.
- **Where to go next.** Buy by cost per cookie per second and click the golden cookie: each is a new function behind the same ports.
