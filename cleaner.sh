#!/usr/bin/env bash

for f in *; do
	if [ -d "$f/Accepted" ]; then
		cd "$f/Accepted"
		latest=$(ls -t | head -1)
		cp "$latest/Solution.py" ../../"$f.py"
		cp "$latest/Solution.cpp" ../../"$f.cpp"
		cd ../..
	fi
	if [ "$f" == ".gitignore" ] || [ "$f" == "cleaner.sh" ] || [ "$f" == "README.md" ]; then
		continue
	fi
	rm -rf "$f"
done
