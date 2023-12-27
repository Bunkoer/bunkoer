
# 🔒🛡️ Bunkoer: Enhancing LLM Application Deployment and Security

**"Empowering Ethical AI and Data Anonymization in LLM Applications"**

## 🚧 Active Development Alert for Bunkoer

Bunkoer, our cutting-edge framework for ethical AI and secure LLM applications, is evolving rapidly. This active development phase means features may change, but we're committed to stability and reliability. Keep up with our updates for the best experience, and proceed with testing before deploying in production environments.

## Quick and Easy Installation

Get Bunkoer up and running with a simple pip command:

```bash
pip install bunkoer
```

### OpenAI API Key Requirement

Bunkoer requires an OpenAI API key to function. Set your key in your environment variables:

```bash
export OPENAI_API_KEY=your_api_key_here
```
*Replace `your_api_key_here` with your actual OpenAI API key.*

### Run your interface

Get a Ui for making all you test:

```bash
python3 -m bunkoer
```
With this ui you can have a secure anonimized chat and work with pdf and csv file safely
*Disclamer we are not responsable of the security of your data*

## ⚙️ Introducing Bunkoer

Bunkoer is not just a library; it's a gateway to secure, ethical AI development. Our framework is built to:

- **Safeguard Privacy**: We integrate advanced anonymization techniques to protect sensitive data within AI models.
- **Promote Ethical AI Practices**: Bunkoer ensures that AI models adhere to ethical standards, focusing on privacy and responsible data handling.

![Bunkoer's Working Schema](images/schema.png)

## Bunkoer's Core Features

- **Modular and User-Friendly**: Customize your AI models with our easy-to-integrate privacy tools.
- **Anonymization Made Simple**: Our pre-configured solutions streamline the privacy process for your data.

## Utilizing Bunkoer

### Secure Your Data Files

Anonymize files effortlessly, starting with CSV formats. Here's how:

```python
from bunkoer.security import SecureFile 

file_path = "/path/to/your/file.csv"
secured_file = SecureFile(file_path)
```

*Note: Bunkoer is in testing phase. Data exposure risks exist.*

### Practical Applications

Secure data can be used in various scenarios, including processing with ChatGPT. Explore more at our [Bunkoer x Streamlit](https://github.com/Bunkoer/bunkoer-x-streamlit) repository.

### Future Developments

- Additional file type support: JSON, SQL
- Enhanced anonymization API


### How Bunkoer Secures Your Data
Bunkoer employs a unique technique of contextual anonymization to safeguard your files, making them safe for exposure in any environment. The process begins with Bunkoer scanning your file to identify different categories of data (for example, in a CSV file, these categories would typically be represented by the headers). Once these categories are identified, they are sent to a GPT model, which determines, based on the context of the categories, whether any category might contain confidential information. If a category is flagged as containing confidential data, it is sent back to your local machine. Bunkoer then proceeds to erase this confidential data from your local machine. This ensures that your sensitive data never leaves your device. With the newly anonymized file created by Bunkoer, you can perform various tasks without compromising data security.

### Definition of Confidential Data by Bunkoer
For Bunkoer, confidential data refers to any information that could potentially be used to identify a person either online or in real life, such as names, phone numbers, IP addresses, etc. The goal of anonymization is not to obscure too much information but to maintain the utility of the data for work and analysis.

### Situations Where Bunkoer May Not Work
- The file is in an unsupported format or is poorly formatted.
- The categories within your file are not clearly defined or explicit.

### Development Status of Bunkoer

Please note that Bunkoer is currently under development. As with any evolving technology, there may be instances where the results are not entirely accurate or as expected. We are continually working to improve Bunkoer's algorithms and functionalities. Your feedback during this development phase is invaluable and will help us refine the tool to better meet your data security needs.

This note acknowledges the ongoing development status of Bunkoer and sets realistic expectations about its current performance.

## Engage with Us

For inquiries or collaboration, open an issue on GitHub, or connect with us on [LinkedIn](https://www.linkedin.com/company/bunkoer/) or via email at bunkoer@bunkoer.com.

## Bunkoer License

We grant free use of Bunkoer under specific conditions, detailed in our license agreement. Commercial use requires a separate agreement. Contact us at bunkoer@bunkoer.com for commercial licenses.

*Disclaimer: Bunkoer is provided "as is". We're not liable for any damages arising from its use.*
