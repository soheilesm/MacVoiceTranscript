#!/bin/bash

printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' -
echo "installing 'portaudio' ..."
echo "============================="
brew install portaudio

printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' -
echo "installing 'elasticsearch' ..."
echo "============================="
brew install elasticsearch

printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' -
echo "installing 'SpeechRecognition' ..."
echo "============================="
pip install SpeechRecognition

printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' -
echo "installing 'elasticsearch' ..."
echo "============================="
pip install elasticsearch

printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' -
echo "installing 'pyaudio' ..."
echo "============================="
pip install pyaudio

printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' -
echo "installing 'espeak' ..."
echo "============================="
brew install espeak
