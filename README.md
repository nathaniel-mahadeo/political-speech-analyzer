# Political Speech Analysis Project

## Project Overview
This project analyzes political speeches in JSON format to examine word frequency, predefined issue keyword counts, and keyword-based sentiment. It processes raw speech transcripts and creates three charts showing patterns in political language.

---

## Getting Started

### Requirements

- Python: tested with Python 3.12.14.
- Matplotlib: the only external package, tested with version 3.10.8.
- The remaining imports use Python's standard library or modules included in this project.

### Installation and Usage (Windows PowerShell)

Open PowerShell in the folder containing `political_speech.py` and the sample JSON files. Install the plotting dependency:

```powershell
py -m pip install -r requirements.txt
```

Run the Obama sample:

```powershell
py political_speech.py obama.json
```

Run either of the other samples:

```powershell
py political_speech.py lbj.json
py political_speech.py trump.json
```

If no filename is provided, the program uses `obama.json` in the current working directory. The program prints its analysis and opens three Matplotlib charts. Close the chart windows to finish the run; they do not close automatically in this version.

On macOS or Linux, use `python3` in place of `py`.

### Running Tests

```powershell
py -m unittest -v political_speech_test.py
```

The project includes seven unit tests covering text cleaning, tokenization, normalization, filtering, frequency counting, issue counting, and sentiment. Specify the test filename: its current name does not match the default `test*.py` discovery pattern.

### Example Output

The included `obama.json` produces these results with the current code and keyword lists:

```text
Total words (raw):      6877
Total words (filtered): 3304
Economy keyword count: 157
Positive words:        135
Negative words:        71
Sentiment score:       0.311
```

The sentiment score is calculated as `(positive_count - negative_count) / (positive_count + negative_count)`. It returns zero when no sentiment keywords are found. A score of zero can also mean that the positive and negative counts are equal; it does not establish that a speech is neutral.

---

## Input Format and Sample Data

Each input file must contain a JSON object. The program reads `title`, `date`, and `transcript`; any other fields are ignored. The transcript should be a string.

```json
{
  "title": "Example Political Speech",
  "date": "2026-01-01",
  "transcript": "We support opportunity, education, and economic growth."
}
```

The included sample files contain speeches attributed in their metadata to Barack Obama, Lyndon B. Johnson, and Donald Trump. The Obama and Johnson files contain Miller Center source URLs:

- `obama.json`: [Miller Center: 2013 State of the Union Address](https://millercenter.org/the-presidency/presidential-speeches/february-13-2013-2013-state-union-address).
- `lbj.json`: [Miller Center: 1967 State of the Union Address](https://millercenter.org/the-presidency/presidential-speeches/january-10-1967-state-union-address).
- `trump.json`: the supplied file does not include a source URL. Its provenance needs to be recorded before describing it as a verified source.

Titles and dates are printed from the supplied JSON metadata; this program does not independently verify them.

---

## Project Files

| File | Purpose |
| --- | --- |
| `political_speech.py` | Main command-line program |
| `loader.py` | JSON loading, text cleaning, and tokenization |
| `analyzer.py` | Word frequencies, issue counts, and sentiment |
| `constants.py` | Stopwords and issue/sentiment keyword lists |
| `plotter.py` | Three Matplotlib charts |
| `political_speech_test.py` | Seven unit tests |
| `requirements.txt` | External package dependency |
| `.gitignore` | Python cache, environment, and editor exclusions |
| `obama.json`, `lbj.json`, `trump.json` | Sample speech inputs |

---

## Relevant Data Structure Concept
The most relevant data structures used in this project are:
- **Dictionaries (hash tables)**
- **Sets**
- **Lists**
- **Collections (Counter)**

---

## Application of Data Structures

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
   - `show_plots()` displays the graphs and waits for the windows to be closed

5. **political_speech.py**
   - Acts as the main controller
   - Calls all modules in sequence
   - Prints formatted output and triggers visualizations

---

## Performance

The main analysis passes are approximately linear in the number of tokens under typical average-time hash table assumptions and bounded word lengths. Let *n* be the number of tokens, *k* the number of issue categories, and *c* the number of transcript characters:

- Text cleaning and tokenization: approximately O(c).
- Filtering, frequency counting, and sentiment counting: approximately O(n).
- Issue counting: O(n × k), with seven predefined categories in this version.
- Top-word selection: additional work depending on the number of distinct words and the requested result count. The main program requests 15 words.

These estimates describe the analysis steps, not the time spent opening charts or waiting for the user to close them. The program stores token lists and frequency tables in memory. No timing benchmark is included in this upload.

---

## Limitations

- Sentiment uses manually selected positive and negative keywords. It does not account for negation, sarcasm, sentence context, or the speaker's intended meaning.
- Issue counts measure keyword occurrences, not verified policy positions or the percentage of a speech devoted to an issue. Broad keywords can match unrelated contexts, and categories can overlap.
- Simple normalization can distort words and cause missed matches. For example, `crisis` becomes `crisi`, which is absent from the negative keyword set. `emissions` becomes `emission`, and `allies` becomes `ally`, which are absent from their issue sets. `rights` becomes `right`, which is then removed as a stopword. These behaviors remain in this version.
- Tokenization keeps only the letters a-z. It drops numbers and does not properly support accented or non-English text.
- The program analyzes one speech per run. Raw counts depend on speech length and should not be treated as directly comparable measures of emphasis across speeches.

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