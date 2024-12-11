# **README: Quran Search Application**

## **Overview**
The Quran Search Application is a user-friendly platform that enables individuals to explore Quranic verses through keyword-based search functionality. The application combines a responsive interface with a robust back-end to deliver precise results efficiently. A semantic search engine has also been implemented on the back-end to enhance search accuracy, though its integration with the front-end remains a future enhancement.

---

## **Features**
1. **Keyword-Based Search**
   - Enables users to search Quranic verses by entering specific keywords.
   - Results include Surah name, Revelation Type, Ayah number, and the complete Ayah text.

2. **User Feedback**
   - Provides clear messages for successful searches and helpful error messages for invalid inputs or technical issues.

3. **Semantic Search Engine**
   - A semantic search engine has been implemented to understand the intent behind user queries and enhance result relevance.
   - Currently, this feature operates on the back-end and is not yet connected to the user interface.

---

## **Core Functionalities**
1. **Search Results Display**
   - Comprehensive details for each verse, including:
     - Surah Name
     - Revelation Type (Meccan or Medinan)
     - Ayah Number
     - Full Ayah Text

2. **Error Handling**
   - Informative feedback for scenarios such as:
     - "An error occurred while fetching data" for back-end issues.

---

## **How to Use**
1. Open the application in a web browser.
2. Enter a keyword (e.g., *mercy*) in the search bar.
3. Click on the **Search** button to retrieve results.
4. View the displayed verses or feedback messages.

---

## **Benefits**
1. **User Accessibility**
   - Intuitive design ensures ease of use for individuals of all technical backgrounds.

2. **Future Scalability**
   - The inclusion of semantic search paves the way for advanced functionality in subsequent iterations.

3. **Educational Impact**
   - Encourages users to engage deeply with the Quran and explore its themes.

4. **Customizability**
   - Built to accommodate future enhancements, including front-end semantic search integration and additional features.

---

## **Challenges and Resolutions**

### **1. JavaScript Proficiency**
   - **Challenge:** Limited experience in JavaScript made implementing dynamic front-end features difficult.
   - **Solution:** Focused on essential concepts, successfully delivering a functional application while gaining proficiency in the language.

### **2. Semantic Search Integration**
   - **Challenge:** Initial models showed poor performance with Arabic text, reducing search accuracy.
   - **Solution:** Replaced the model with a more suitable pre-trained alternative tailored for Arabic.

   - **Challenge:** OpenAI’s API was unavailable due to time constraints.
   - **Solution:** Opted for Hugging Face’s locally hosted models, ensuring efficiency and cost-effectiveness.

### **3. Data Formatting**
- **Challenge:** Extracting and structuring key information from the Quran API for clear presentation in the front-end.
- **Solution:** Processed and simplified the API response in the back-end to include only relevant details for display.

### **4. Error Management**
   - **Challenge:** Handling invalid user inputs and system errors effectively.
   - **Solution:** Designed user-friendly error messages to provide clear guidance and reassurance.
