# Mygpt

This is a simple chatbot using the OpenAi api, the general idea of this project is to save me the fatigue of answering interviewers. 

This is the architecture of this project
```bash
/mygpt
│
├── app.py code of chatbot with Flask
├── .env use this file for use key API of OPENAI.
├── .gitignore 
├── templates
│   └── index.html 
├── static
│   └── styles.css 
└── README.md
```
## How to install 

First, clone this repository at your computer
```bash
git clone https://github.com/yourusername/mychatbot.git
```
Then, navigate to the project directory:
```
cd mygpt
```
Install the necessary dependencies:
```
pip install flask openai python-dotenv
```
Create an .env file in the root directory of the project and add your OpenAI API key:
```
echo "OPENAI_API_KEY=your-openai-api-key" > .env
```
To excute the chatbot, use next command
```
python app.py
```
Later, open your browser and navigate to http://localhost:5000 to interact with the chatbot.

##  Contribution
Contributions are welcome. Please open an issue or pull request for suggestions or improvements.

## License
This project is licensed under the MIT License - see the Licence file for details.