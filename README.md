# Discord-Bot

The simple multi purpose discord bot

<p align="center">
    <img src="https://raw.githubusercontent.com/hirusha-adi/yourbot/main/images/background4.gif" alt="BACKGROUND_IMAGE">
    <br>
    <img src="https://img.shields.io/github/license/hirusha-adi/Discord-Bot" alt="Lisence">
    <img src="https://img.shields.io/github/last-commit/hirusha-adi/Discord-Bot" alt="Last Commit">
    <img src="https://img.shields.io/github/contributors/hirusha-adi/Discord-Bot" alt="Contributors">
</p>
<!-- Discord-Bot -->

## Folder Structure

- `./` (Parent Directory)
  - `yourbot`
    - `assets`
      - `tools`
        - `utils.py` (handling settings for each and every discord server)
      - Other files (fonts, password_lists, images for PIL)
    - `cogs`
      - musicplayer
        - Files (this is the Music cog, it has multiple files)
      - Others (cogs for yourbot, all the .py files (cogs) in this folder will be loaded automatically)
    - `database`
      - `announcements`
        - Files (including the database itself(its just a text file lmao) with a manager (getter, sort of) for it)
      - `blacklist`
        - Files (text files with blacklister user and server IDs)
      - `scinfo`
        - Files (for server specific settings and information)
      - Files (mostly managers(getters, sort of) for other databse files)
    - `others`
      - File (mainly for handling dependencies simply and automatically)
    - `web`
      - `templates` (for flask)
        - Files (`*.html` files)
      - `static` (for flask)
        - `js`
          - Files (`*.js` (JavaScript) Files)
        - `css`
          - Files (`*.css` (CSS - Cascase Style Sheet) Files)
        - `fonts`
          - Files (fonts required for the flask website)
        - Files (other python3 files for the flask webserver)
    - Files (main file to start the bot, Lisence, To-do-list, privacy-policy, other git files)

## Social

- OFFICIAL WEBSITE: https://hirusha-adi.github.io/yourbot/ (this repo will be merged with this in the future)
- OFFICAL DISCORD SERVER: https://discord.gg/dEPJ2t6mqQ
