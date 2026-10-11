# Political Speech Analysis Project

## Project Overview
This project analyzes political speeches in JSON format to extract meaningful insights such as word frequency, issue prevalence, and sentiment. It processes raw speech transcripts and visualizes patterns in political language.

---

## Relevant Data Structure Concept
The most relevant data structures used in this project are:
- **Dictionaries (hash tables)**
- **Sets**
- **Lists**
- **Collections (Counter)**

---

## 2.1 Application of Data Structures

- **Dictionaries (Hash Tables)**  
  - Used in `analyzer.py` (`build_frequency_table()`) to map words → frequency counts  
  - Used in `analyzer.py` (`count_issues()`) to map issue categories → keyword counts  
  - Used in `constants.py` (`ISSUES`) to map each issue → set of keywords  
  - Provide **O(1)** average-time insertion and lookup for efficient counting  

- **Sets**  
  - Used in `constants.py` (`STOPWORDS`, `POSITIVE_WORDS`, `NEGATIVE_WORDS`) for fast membership checking  
  - Used in `analyzer.py` (`filter_words()`) to remove stopwords efficiently  
  - Used in `analyzer.py` (`count_issues()`) to check if a word belongs to an issue category  
  - Provide **O(1)** average-time membership checks  

- **Lists**  
  - Used in `loader.py` (`tokenize()`) to store sequences of words from the transcript  
  - Used in `analyzer.py` to pass word sequences through filtering and analysis steps  
  - Used in `plotter.py` to store labels and values for visualization  
  - Allow ordered traversal of words for sequential processing  

- **Collections (Counter)**  
  - Used in `analyzer.py` (`top_n_words()`) to efficiently retrieve the most frequent words  
  - Built on top of dictionaries for optimized counting and sorting  

---

## Project Workflow

### Input
- A JSON file containing a political speech (title, date, transcript)

### Processing Pipeline (by script)

1. **loader.py**
   - `load_speech()` loads the JSON file into a dictionary
   - `strip_html()` removes HTML tags and formatting
   - `tokenize()` converts the cleaned text into a list of lowercase words

2. **analyzer.py**
   - `normalize_word()` applies simple word normalization (e.g., plural handling)
   - `filter_words()` removes stopwords using a set
   - `build_frequency_table()` creates a dictionary mapping words → counts
   - `top_n_words()` extracts the most frequent words using `Counter`
   - `count_issues()` counts how often words appear in predefined issue categories
   - `compute_sentiment()` calculates positive vs negative word counts and a score

3. **constants.py**
   - Stores:
     - `STOPWORDS` (set for filtering)
     - `ISSUES` (dictionary mapping issue → keyword sets)
     - `POSITIVE_WORDS` and `NEGATIVE_WORDS` (sets for sentiment)

4. **plotter.py**
   - `plot_issue_counts()` creates a bar chart of issue frequencies
   - `plot_top_words()` creates a bar chart of most frequent words
   - `plot_sentiment()` visualizes positive vs negative word counts
   - `show_plots()` displays (or auto-closes) the graphs

5. **political_speech.py**
   - Acts as the main controller
   - Calls all modules in sequence
   - Prints formatted output and triggers visualizations

---

## Performance
The overall time complexity of the project is approximately **O(n)**, where *n* is the number of words in the speech.

- Tokenization: O(n)  
- Filtering: O(n)  
- Frequency counting: O(n)  
- Issue counting: O(n × k), where *k* is the number of issue categories (constant)  

Since all major operations involve single passes through the data, the program performs efficiently even on long speeches.

---

## Challenges
One challenge was handling inconsistent text formatting from raw transcripts, such as HTML tags and special characters. This was addressed by implementing a cleaning function using regular expressions.

Another challenge was designing a simple but effective normalization approach (e.g., handling plural words). This required balancing accuracy with simplicity without using external NLP libraries.

A significant challenge was filtering and categorizing words into meaningful groups, particularly for sentiment and issue classification. Determining which words should be considered “positive” or “negative” is inherently subjective and context-dependent. For example, words like "strong" or "growth" are generally positive, but their meaning can change depending on context. Similarly, deciding which words belong in issue categories (such as economy or healthcare) required careful selection to avoid overcounting or missing relevant terms.

Additionally, creating the constant sets (e.g., STOPWORDS, POSITIVE_WORDS, NEGATIVE_WORDS) involved balancing completeness with performance. Including too many words could dilute the analysis, while including too few could reduce accuracy. These sets were refined iteratively by testing the program on real speech data and adjusting based on observed outputs.

---

## Improvements
If I were to redo or expand this project, I would incorporate more advanced natural language processing techniques, such as stemming or lemmatization, to improve word normalization and overall accuracy. I would also expand the sentiment analysis by using weighted scoring systems or external datasets to better capture nuance in language.

Another potential improvement would be adding support for analyzing multiple speeches at once, allowing for comparisons across speakers, time periods, or political parties. This could provide deeper insights into how rhetoric changes over time.

A more advanced and creative extension would be to incorporate a **voice analysis feature**. In this version, a user could speak into a microphone, and the program would analyze their speech patterns, word choice, and tone. The system could then compare this input to a dataset of well-known speakers (e.g., political leaders or celebrities) and return the individual whose speaking style most closely matches the user. This would require integrating speech-to-text processing and possibly machine learning techniques for pattern recognition.

Additionally, the user interface could be improved by creating an interactive application (such as a GUI or web app) where users can upload files, select analysis options, and view results dynamically. These improvements would make the project more user-friendly and extend its real-world applicability.

---

## Learning
Through this project, I strengthened my understanding of:
- How data structures like dictionaries and sets improve efficiency
- Text processing and tokenization techniques
- Writing modular Python programs
- Using visualization libraries to present data
- Designing and running unit tests for validation

---

## Real-World Relevance
This project has applications in:
- Political analysis (tracking themes and rhetoric)
- Media and journalism (speech analysis)
- Sentiment analysis in social media or public statements
- Natural language processing pipelines
- Data-driven decision making in policy or communications

---

## Use of AI Tools
AI tools were used to:
- Brainstorm project structure and features
- Debug issues in code and unit tests
- Improve code readability and organization
- Assist in generating documentation and refining explanations

All core logic and design decisions were understood and implemented by the developer.