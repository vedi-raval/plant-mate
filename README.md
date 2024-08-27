# PlantMate

### Description

Plant Mate is a plant recommendation chatbot that leverages Generative AI to create customized recommendations for users of plants they can grow. The user can input any information regarding their planting needs, ranging from plot size, to weather, and even the kinds of plants they would prefer to grow. Once Plant Mate curates responses to the user's preferences, the user can ask Plant Mate to elaborate on any of the advice that they receive, even asking for further recommendations. The chatbot has streaming and memory of previous aspects of the conversation that it can leverage throughout the chat.  

### Set-up

The application uses an OpenAI key, thus one of the first steps in the set up was getting the key from OpenAI. Once the key was set up, I then had to install Chainlit in order to have a chatbot with both a back-end conversational bot and a functional and aesthetic front end. Along with this, I installed the asyncio library in order to allow myself to write code that can perform multiple tasks at the same time without actually doing them at the same time. 

### Running the application

To run the app, navigate to the root of the project folder and execute the following command in the terminal: 

```
chainlit run plants_recommendation_svc.py -w
```
This will open a seperate browser with Plant Mate.

### Approach

- Install needed packages (OpenAI key, Chainlit, asyncio)
- Code the back end of the chatbot:
    - Implement past conversaton history memory
    - Implement an initial message that gets loaded in automatically
    - Stream tokens to deliver content to the user as soon as available
    - Prompt engineering - the chatbot knows what it is supposed to answer and how
    - Ensure Plant Mate only responds with planting related answers
- Code the front end of the chatbot: Chainlit

### Impact

- Promote Sustainable Gardening Practices: By recommending plant species and garden layouts that align with local climate conditions and available resources, the chatbot encourages environmentally sustainable gardening.
- Foster Inclusivity and Accessibility: The chatbot is designed to be user-friendly and inclusive for all, with features like typo tolerance and robustness to varied inputs, ensuring that a wide audience can benefit from its recommendations.

### Key Benefits

- Personalized Recommendations: The chatbot provides tailored advice based on specific user inputs, ensuring that recommendations are relevant and effective for the user’s unique gardening situation.
- Streamlined Decision-Making: The tool simplifies complex gardening decisions, saving users time and reducing the overwhelm that often comes with planning and maintaining a garden.
- Environmental Impact: By promoting the use of native plants and water-efficient gardening practices, the chatbot contributes to the conservation of natural resources and supports local ecosystems.
- Content Guardrails: PlantMate only focuses on gardening ideas and does not respond to other requests that may be inappropriate for its use case 

### Future Potential

The gardening recommendation chatbot has the potential to evolve into a comprehensive gardening companion, incorporating features such as real-time weather updates, integration with gardening apps, and expanded databases of plant species. As it grows, the chatbot will continue to serve as a valuable resource for individuals and communities looking to enhance their green spaces.

