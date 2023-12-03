# 🔒🛡️ Bunkoer

⚡  Building secure LLM applications through composability ⚡

# Warning: Library Under Active Development

Please be aware that this library is currently under active development. As such, it is subject to frequent updates and changes. While we strive to ensure stability and reliability, rapid evolution means that certain features or behaviors may change without prior notice. We encourage users to stay updated with the latest version, but also advise caution and thorough testing before using this library in production environments.


## Quick Install

With pip: 

```
pip install bunkoer
```

## ⚙️ What is Bunkoer?

Bunkoer is a framework designed to secure the development of applications powered by large language models. It facilitates solutions that:

- Ensure Privacy: Bunkoer links AI models with mechanisms to safeguard sensitive information (through anonymization techniques, privacy-preserving prompts, etc.)
- Foster Ethical AI: leans on AI models to uphold ethical standards (by evaluating and modifying responses to maintain privacy, determining appropriate data handling actions, etc.)

![Schema](images/schema.png)

## How Does Bunkoer Help? 

The core strengths of the Bunkoer framework are:

- **Modular Features**: Tailored tools and integrations for enhancing data privacy in AI models. These features are designed to be both modular and user-friendly, applicable within and beyond the Bunkoer framework.
- **Pre-configured Anonymization Processes**: Ready-made combinations of features aimed at achieving higher-level privacy tasks.
  
## How to use it ?

### Secure your files !
Using security feature of bunkoer you can anonymize any type of file (actually only available for csv file) without expoxing any confidential data, for exploit it as you which.

With python :
```
#Import the security module of bunkoer
from bunkoer.security import SecureFile #This function going to find and anonymized content that can be dangerous to expose

file_path = "/path/to/your/file" #The file you want to securise 
test = SecureFile(file_path) #The SecureFile function return a the path of the anonimized file
```

[Warning] The bunkoer lib is still developemnt and testing, sometimes the anonimization can be incorect. We are not responsable if you exposed you data 
- Use case :
  Now your data are secure and you can use it for any type of things. For example you can process your data on chat GPT.
  For doing this you can simply use our repository [bunkoer x streamlit](https://github.com/Bunkoer/bunkoer-x-streamlit)


Coming Soon :
- Type of file : json, sql
- Streamliy anonimization api 

### Optimize your anonymized file !
- Coming soon

## License 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Bunkoer Software"), to deal in the Bunkoer Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Bunkoer Software, and to permit persons to whom the Bunkoer Software is furnished to do so, subject to the following conditions:

Commercial Clause: Notwithstanding the above, the use of the Bunkoer Software for commercial purposes is conditioned upon the conclusion of a separate commercial license agreement. "Commercial use" refers to the use of the Bunkoer Software in a product or service that is sold, rented, or used for the purpose of generating revenue. To negotiate a commercial license agreement, please contact us at bunkoer@bunkoer.com.

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Bunkoer Software.

THE BUNKOER SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE BUNKOER SOFTWARE OR THE USE OR OTHER DEALINGS IN THE BUNKOER SOFTWARE.
