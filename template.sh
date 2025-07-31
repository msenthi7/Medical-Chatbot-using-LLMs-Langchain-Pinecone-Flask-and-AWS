# Creating directories
# (-p is parameter)
mkdir -p src
mkdir -p research


# Creating files
# touch command creates new file
touch src/__init__.py # treated as package, for importing modules
touch src/helper.py # utility fns (user-defined) are stored here;
touch src/prompt.py # contains definitions for prompts used with large language models (LLMs)
touch .env # store environment variables like api keys,,db credentials, etc; rather than us writing it in the code (since they might be sensitive and might require configurations)
touch setup.py #  It contains metadata about your project (name, version, author, description) and instructions on how to install it. pip install executes this file
touch app.py # This is commonly the main entry point for your application. When you run your program, you would typically execute this file
touch research/trials.ipynb # for experimentation, exploratory work
touch requirements.txt # This file lists all the third-party Python packages and their specific versions 

echo "Directory created successyully"

# run it in terminal or gitbash to execute this file; 
# sh template.sh is the command


