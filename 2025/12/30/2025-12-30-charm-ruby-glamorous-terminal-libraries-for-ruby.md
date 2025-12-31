# Charm Ruby – Glamorous Terminal Libraries for Ruby

- Score: 128 | [HN](https://news.ycombinator.com/item?id=46430558) | Link: https://charm-ruby.dev/

## TL;DR
Charm Ruby is a collection of Ruby ports and bindings for the Charmbracelet TUI ecosystem, bringing Bubbletea, Bubbles, Lipgloss, Glamour, NTCharts, Gum, Harmonica, Bubblezone, and Huh to Ruby 3.2+. It lets Ruby developers build Elm-architecture TUIs, styled output, forms, markdown renderers, animations, and real-time terminal charts, with concise example code. HN discussion is enthusiastic but notes the APIs currently mirror Go rather than idiomatic Ruby, with calls for richer DSLs and layout/theming abstractions.

## Comment pulse
- Excitement from Charm and Ruby users → Ruby TUI options felt dated; this stack promises modern, expressive CLIs without leaving the language.
- API design debate → some find the examples un-Rubyish and want metaprogrammed DSLs—counterpoint: first release deliberately mirrors Go and Elm-core concepts.
- Requested features → CSS-like grid/flex layouts and a shared visual config spec; Lipgloss is seen as a partial answer for style consistency.

## LLM perspective
- View: Strong base: mature Go libraries plus Ruby bindings; next step is embracing Ruby’s syntax for higher-level, opinionated DSLs.
- Impact: Could shift many internal tools from ad-hoc scripts or web UIs to richer TUIs, especially for Ruby-centric teams.
- Watch next: Ruby-specific layouts, theming standards, and API refactors; also performance and portability of the Go-linked C extensions.
