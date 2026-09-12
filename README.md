# Notes.py — a terminal notebook with its own encoding and account system

![status](https://img.shields.io/badge/status-archived-lightgrey)
![stack](https://img.shields.io/badge/stack-Python%203-3776AB)
![deps](https://img.shields.io/badge/dependencies-standard%20library%20only-informational)
![from-scratch](https://img.shields.io/badge/built-without%20AI%20assistance-orange)
![license](https://img.shields.io/badge/license-MIT-blue)

> Written entirely by hand, without AI assistance — one of only two
> projects in my portfolio built that way.

A command-line note-taking app that organizes entries into named
chapters, gates access behind a personal account system, and stores
everything through a custom character-level encoding scheme instead of
plain text — all using nothing but Python's standard library (`os`,
`math`).

## Why this project is on my resume

This isn't the most polished project in my portfolio, and it isn't meant
to be — it's the one that shows raw problem-solving without a framework,
a library, or AI pair-programming to lean on:

- **A homemade encoding scheme, designed and debugged from scratch.**
  `to_Binary()` maps each character to `ord(char) ** 2`, converts that to
  binary by hand (no `bin()`), and joins the codes space-separated.
  `de_code()` reverses it: parse each binary group back to an integer,
  `sqrt()` it, and `chr()` it back to the original character. It's not
  cryptography — it's a from-first-principles exercise in thinking about
  data as transformable bits rather than reaching for a library.
- **A real, if minimal, account system on flat files.** Usernames and
  passwords are validated with hand-written rules (`check_valid`,
  `valid_check`), matched against an encoded `database.txt`, and each
  user's chapters live in their own file under `NOTES(Database)/Accounts`,
  named by splicing halves of their username and password together
  (`file_name`) — a self-taught approach to per-user data isolation
  without any actual database.
- **Defensive, hand-rolled input loops everywhere.** Every input — a
  username, a password, a chapter title — is validated in a `while` loop
  that keeps re-prompting with a specific reason ("not start with a
  space," "at least 3 letters," "not start with a digit") until it's
  valid, rather than trusting the caller or crashing on bad input.

## What it does

- **Create an account** — username and password validated at entry time,
  stored (encoded) in a shared database file, with a dedicated per-user
  data file created automatically.
- **Log in** — matches the entered, re-encoded credentials against the
  stored records, with a limited number of retry attempts before the
  session closes.
- **Chapters** — once logged in, a user can:
  - Add a new chapter
  - Add text between existing lines in a chapter
  - Edit a chapter — replace words in a line, remove words in a line, or
    remove a whole line
  - Delete a chapter
  - Display one chapter or all chapters at once
- **Account management** — forgot-password recovery, change password
  (re-encodes and rewrites the user's record in place), and delete account
  (removes both the shared-database entry and the user's private data
  file).
- **A menu-driven terminal UI** — nested menus for the main flow, the
  logged-in note actions, and the edit sub-actions, each with its own
  numbered options and a help screen.

## How data is stored

```
NOTES(Database)/
├── database.txt          One encoded line per registered user
└── Accounts/
    └── <spliced-name>.txt   One file per user, holding their encoded
                              chapters and content
```

Nothing is stored as plain text — every line written to disk goes through
`to_Binary()` first and is reversed with `de_code()` on read, including
usernames, passwords, and note content itself.

## Run it

```bash
python3 Notes.py
```

No dependencies beyond the Python standard library. On first run, it
creates its own `NOTES(Database)` folder (and an `Accounts` subfolder) in
the current working directory.

## Honest limitations

- The encoding is **not real security** — `ord(char) ** 2` → binary → 
  `sqrt()` → `chr()` is a reversible, deterministic transform with no key,
  salt, or cryptographic guarantee. It obscures plain text from a casual
  glance at the file, nothing more.
- Data is per-machine, flat-file, and single-process — there's no
  concurrent-access handling, no backup/export, and no recovery beyond the
  built-in "forgot password" flow.
- This project predates my move to structured, tested, framework-based
  projects — it's included specifically to show the foundational,
  unassisted problem-solving those later projects build on.
