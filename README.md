# Canvas Chatbot Template

This is a simple Flask-based chatbot template using the OpenAI API, designed to integrate with Canvas LMS.

## Launch in Codespaces
[![Open in Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?template_repository=YOUR-USERNAME/canvas-chatbot)

## Structure

- `chatbot.py`: Chat wrapper for OpenAI
- `app.py`: Flask web server with POST endpoint
- `.env`: API key (edit this in Codespace)
- `.devcontainer/`: GitHub Codespace config

## Quick Start

```bash
flask run --host=0.0.0.0
