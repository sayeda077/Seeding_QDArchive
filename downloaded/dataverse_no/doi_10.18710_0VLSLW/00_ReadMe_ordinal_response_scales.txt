This README file was generated on 2024-2-28 (YYYY-MM-DD) by Lukas Sönning.
Last updated: 2024-09-20.


-------------------
GENERAL INFORMATION
-------------------

// Title of dataset: Background data for: Ordinal response scales: Psychometric grounding for design and analysis
// DOI: https://doi.org/10.18710/0VLSLW
// Contact Information
     // Name: Lukas Sönning
     // Institution: University of Bamberg
     // Email: lukas.soenning@uni-bamberg.de
     // ORCID: https://orcid.org/0000-0002-2705-395X
 
// Kind of data: See metadata field Kind of Data.
// Date of data collection/generation: See metadata field Date of Collection.
// Geographic location: See metadata section Geographic Coverage.
// Funding sources: See metadata section Grant Information.

// Description of data set: 
This dataset contains background data and supplementary material for a methodological study on the use of ordinal response scales in linguistic research. For the literature survey reported in that study, which examines how rating scales are used in current linguistic research (4,441 papers from 16 linguistic journals, published between 2012 and 2022), it includes a tabular file listing the 406 research articles that report ordinal rating scale data. This file records annotated attributes of the studies and rating scales. Further the dataset includes summary data gathered in a review of the psychometric literature on the interpretation of quantificational expressions that are often used to build graded scales. Empirical findings are collected for five rating scale dimensions: agreement (1 study), intensity (3 studies), frequency (17 studies), probability (11 studies), and quality (3 studies). Finally, the post includes new data from 20 informants on the interpretation of the quantifiers "few", "some", "many", and "most".  


--------------------------
METHODOLOGICAL INFORMATION
--------------------------

(1) Data on the perception of quantifiers 

To obtain data on the perception of the quantifiers "few", "some", "many", and "most", a short survey was conducted, using as participants students and staff associated with the department of English Linguistics at the University of Bamberg. Responses were collected from 20 individuals (around 2/3 being students) by handing out paper slips (see file "quantifier_perception_task.png") with the following instructions:

This is a short survey on the interpretation of quantifiers (e.g. "some", "many"). Picture a group of 100 people. How many individuals are – in your view – approximately referred to by the following phrases?

few people:	_____
some people:	_____
many people:	_____
most people:	_____

Participants were given two minutes to complete the task. 


(2) Data from the literature survey on the use of rating scales in linguistic research

To gain an overview of the use of rating scales in linguistic research, we examined all articles published between 2012 and 2022 in 17 linguistic journals (4,441 publications in total), which range broadly across subfields and methodologies. With the exception of some special issues, all research articles that appeared between 2012 and 2022 were included (N refers to the number of articles):

    N  Journal
  ---  ------------------------------------------------
  557  Applied Psycholinguistics
  391  World Englishes
  378  Linguistics
  372  Applied Linguistics
  352  Natural Language and Linguistic Theory
  346  Language Learning
  310  Studies in Second Language Acquisition
  250  English Language and Linguistics
  239  Language
  210  International Journal of Corpus Linguistics
  195  Cognitive Linguistics
  191  Journal of Sociolinguistics
  152  Language Variation and Change
  151  Corpus Linguistics and Linguistic Theory
  148  Corpora
  126  English World-Wide
   73  International Journal of Learner Corpus Research

The qualitative data analysis software MAXQDA 2022 (VERBI Software 2021) was used to conduct the survey. The search terms "rating scale", "rating task", "judg(e)ment task", "ordinal", "Likert", and "semantic differential" served to identify potentially relevant documents, yielding n = 909 hits. We then manually identified those articles that employed an ordinal rating scale (n = 405), where informants indicate some kind of assessment by choosing from an ordered set of categories. If a study employed different rating scale formats, each layout entered our survey, yielding a greater number of rating scales (n = 473) than articles in our database. Differences had to occur along (one of) the features of main interest in our survey: number of response categories, the incorporation of verbal labels, and the underlying dimension. These 473 rating scales were annotated for a number of variables. Apart from attributes of the study (journal, year, DOI), these were predominantly properties of the rating scale, including (i) a short description of the variable that was measured, (ii) the role played by that variable in the research design (outcome, predictor, etc.), (iii) whether the rating scale formed part of a multi-item instrument, (iv) the scale labels used, (v) the way in which verbal labels were incorporated into the scale, (vi) the number of response categories, and (vi) the analysis strategy used. Further, rating scales were classified according to the underlying dimension that effects the rank order. Following Rohrmann (2007), five major dimensions were distinguished:

* Intensity: Intensifying adverbs denote different degrees to which a certain attribute is present (e.g. slightly/quite acceptable). 
* Agreement: The widely familiar Likert-type response format  (e.g. strongly/mainly/somewhat disagree), which often involves elements of intensification but forms a separate dimension due to its widespread use and bipolar nature. 
* Frequency: Expressions denote the rate at which something happens (e.g. rarely, frequently). 
* Probability: Phrases reflect the likelihood of some event (e.g. unlikely, probable). 
* Quality: A good-bad continuum, which may also draw on intensifiers but typically relies on different adjectives (e.g. poor, fine), making it a dimension in its own right.

These annotations are recorded in the tabular file "survey_rating_scales.tsv".


(3) Data from the review of the psychometric literature on verbal scale point labels

A number of experimental studies have shed light on the interpretation of commonly used rating scale labels. We collected findings reported in the literature and organized these according to the five major dimensions outlined above:
 
// Agreement
For agreement phrases, we rely on the findings in Rohrmann (2007). Subjects in that study performed different tasks, and we selected the "category scaling" one, where expressions had to be placed on an equally-apportioned 11-point scale. This scale is mapped to the [0,10] interval. Rohrmann (2007) collected data from 164 participants (120 psychology students, 44 participants from the "general population"). The results we include here are those for all contexts combined (annoyance by noise, job satisfaction, context-free), which Rohrmann (2007) lists in Table 3-S, in the columns headed "CATEGORIAL". These data are given in the file "literature_results_agreement.tsv".

// Intensity
For the intensity dimension, we summarize the findings of three studies that used similar methods to scale the meaning of intensifying adverbs (Matthews et al. 1978; Krsacok 2001; Rohrmann 2007). These studies asked informants to locate each phrase on an 11-point scale, which we map to the [0,10] interval. 
* The results for Krsacok (2001) are copied from Table 7 (p. 25), where ratings are given separately for male (n = 54) and female (n = 54) college students. We preserve these subgroups. Only the values Krsacok (2001) reported for the head adjective "acceptable" are included here, which means that the labels "acceptable" (without intensifier), "marginal", "neutral" and "borderline" were excluded; likewise, the data for the head adjective "unacceptable" are not included here. To check the consistency of participants' responses, Krsacok (2001) measured the phrase "mildly acceptable" twice, and the values we include here are averages over the two rows in Krsacok's (2001) Table 7. 
* The results for Matthews et al. (1978), whose pool of subjects are n = 51 US Army personnel, are taken from Table 2 (p. 7). Again, only the values for the head adjective "acceptable" are included here -- the labels "acceptable" (without intensifier), "marginal", "neutral" and "borderline", as well as the data for the head adjective "unacceptable" are not included here. 
* Rohrmann (2007) collected data from 164 participants (120 psychology students, 44 participants from the "general population"). Included here are the results Rohrmann (2007) lists in Table 3-I, in the columns headed "CATEGORIAL". 
The data gathered from the literature on the intensity dimension are listed in the file "literature_results_intensity.tsv".

// Frequency and probability; Mosteller & Youtz (1990)
For the dimensions frequency and probability, we largely rely on a study by Mosteller & Youtz (1990), who, in addition to carrying out their own empirical survey, summarized findings reported in 19 other studies. These are listed in Table 1 of Mosteller & Youtz (1990), from which we copied them, adding study metadata that Mosteller & Youtz (1990) list in their references (p. 11-12). Details on these other studies are provided below (see "DATA-SPECIFIC INFORMATION FOR: literature_results_frequency.tsv"). The data from Mosteller & Youtz (1990) are also given separately (file: "results_mosteller_youtz_1990.tsv") as they include information on the variability of responses across subjects. Using a mail questionnaire, Mosteller and Youtz (1990) asked science writers to give the probability they would attach to 52 phrases. Ratings were obtained from around 230 individuals (figures varied somewhat between items). The values included here were copied from Table 2 in Mosteller & Youtz (1990), and the arithmetic means are taken from Table 1 in that paper. Rohrmann (2007) also reported on the frequency dimension (Table 3-F) and the probability dimension (Table 5-P [sic!], columns headed "CATEGORIAL"); data are from 164 participants (see above).

// Quality
For the final dimension, quality, we summarize the findings of three studies that used similar methods to scale the meaning of 50 adjectives (Myers & Warner 1968; Vidali 1975; Wildt & Mazis 1978). Informants were asked to locate each adjective on a 21-point scale, where the endpoints were labeled "the best/worst thing I could say about X". We have again mapped this 21-point scale to the [0, 10] interval. 
* Myers & Warner (1968) report data from four subgroups: housewives (n = 25), business executives (n = 36), graduate business administration students (n = 40), undergraduate business administration students (n = 25). Means and standard deviations are reported for these groups in the table on p. 411, from which we copied the data.
* Vidali (1975) studied undergraduate (n = 22) and graduate students (n = 26), and reports means and standard deviations for these subgroups in Table 1 (p. 23), from which we copied the data. We preserve these subgroups. 
* Wildt & Mazis (1978) studied 54 undergraduate students at the University of Florida. They report their findings (means and standard deviations) in Table 1 (p. 262), from which we copied them.
The data gathered from the literature on the quality dimension are listed in the file "literature_results_quality.tsv".

// Quantifiers
For the interpretation of quantifiers, we found three relevant studies:
* The results in Borges & Sawyers (1974) are reported in graphical form only, so we took approximations from the graphs. For both experiments reported in that paper, we disregarded the smallest set size, 12, and then averaged over the proportions for the remaining set sizes.
* For Experiment 1 in Newstead et al. (1987), we only considered the data for set size 108, which are reported in Table 1 of that paper. For Experiment 2 in that paper, the small set size of 12 was again set aside, and the proportions are averaged over the set sizes 60, 108, and 1000, which all stem from the same 18 participants. Since for the set size 10,000 a new sample of 20 subjects was recruited, we list the proportions reported for these individuals as a separate entry.
* The data from van Tiel et al. (2021) are available online, so we were able to directly access the measurements underlying Figure 1A in that paper (from experiment 1a). Our first step was to obtain, for each participant, the median proportion assigned to each of the four quantifiers. To obtain the typical value assigned to a specific quantifier, we then took the median over these participant medians, which are the proportions listed here.
The data gathered from the literature on the perception of quantifiers are collected in the file "literature_results_quantifiers.tsv".


--------------------
DATA & FILE OVERVIEW
--------------------

// File List: 
* 00_ReadMe_ordinal_response_scales.txt : The present file, containing documentation of the dataset
* data_perception_quantifiers.tsv       : Tab-separated data table, quantifier ratings provided by 20 informants
* data_protection_impact_assessment.pdf : Brief assessment of whether the open publication of the dataset is aligned with applicable legal and research-ethical rules and guidelines
* literature_results_agreement.tsv      : Tab-separated data table, psychometric data in the literature on agreement
* literature_results_frequency.tsv      : Tab-separated data table, psychometric data in the literature on frequency
* literature_results_intensity.tsv      : Tab-separated data table, psychometric data in the literature on intensity
* literature_results_probability.tsv    : Tab-separated data table, psychometric data in the literature on probability
* literature_results_quality.tsv        : Tab-separated data table, psychometric data in the literature on quality
* literature_results_quantifiers.tsv    : Tab-separated data table, psychometric data in the literature on quantifiers
* quantifier_perception_task.png        : Copy of the paper slip used to collect data on the perception of quantifiers
* results_mosteller_youtz_1990.tsv      : Tab-separated data table, summary data from Mosteller & Youtz (1990)
* survey_rating_scales.tsv              : Tab-separated data table, annotated rating scales from literature survey

// Is this a new version of a previously published data set?
No


--------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: data_perception_quantifiers.tsv     
--------------------------------------------------------------

// Variable/Column List: 
* subject    : informant ID
* quantifier : quantifier (i.e. "few", "some", "many", "most")
* percentage : estimated percentage of total referred to by the quantifier

// Missing data code: 
No missing data.


---------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: literature_results_agreement.tsv            
---------------------------------------------------------------

// Variable/Column List: 
* verbal_label         : expression (e.g. "fully disagree", "disagree")
* study_subgroup       : study (subgroup) ID (only "rohrmann2007")
* n_subjects           : number of subjects in study (subgroup) (only 164)
* mean_score           : mean score (11-point scale; rescaled to [0,10])
* sd_score             : standard deviation of scores (11-point scale; rescaled to [0,10])

// Missing data code: 
No missing data.


---------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: literature_results_frequency.tsv            
---------------------------------------------------------------

// Variable/Column List: 
* verbal_label         : frequency expression (e.g. "always", "sometimes", "rarely")
* percentage           : average percentage of total referred to by frequency adverb
* measure              : statistical measure used to express the "average percentage" (mean, median)
* study                : study ID (see [A] below)
* n_subjects           : number of subjects in study

// Missing data code: 
No missing data.

[A] Key to studies (from Mosteller & Youtz 1990: 11-12)

(1) BRYANT, G. D. and NORMAN, G. R. (1980). Expressions of probability: Words and numbers. New England J. Med. 302 411. 
n = 32: 16 physicians responding twice each; averages read from chart. 
(2) BUDESCU, D. V. and WALLSTEN, T. S. (1985). Consistency in interpretation of probabilistic phrases. Organizational Behavior and Human Decision Processes 36 391-405. 
n = 32: faculty and graduate students in psychology, University of North Carolina, Chapel Hill. 
(3) HAKEL, M. D. (1968). How often is often? Amer. PsychoL 23 533-534. 
n = 100: students in an introductory psychology course, University of Minnesota. 
(4) HARTLEY, J., TRUEMAN, M. and RODGERS, A. (1984). The effects of verbal and numerical quantifiers on questionnaire responses. Appl. Ergonomics 15.2 149-155. 
Undergraduate students, University of Keele: n_a = 20 students given one set of expressions. n_b = 20 different students given another set. n_c = 20 students given still another set. a: always, often, occasionalIy, seldom, never. b: always, often, fairly many times, occasionally, never. c: always, quite often, sometimes, infrequently, none of the time. 
(5) HARTSOUGH, W. R. (1977). Assignment of subjective probabilities to verbal probability phrases as a function of locus of control and set conditions. J. Psychology 95 87-97. 
n = 60 (10 each in 6 groups): students in an introductory psychology course. 
(6) JOHNSON, E. M. (1973). Numerical encoding of qualitative expressions of uncertainty. Technical Paper 250, U.S. Army Research Institute for the Behavioral and Social Sciences, AD 780 814. 
n = 28: 14 U.S. Army enlisted men and 14 extension college students. 
(7) KENNEY, R. M. (1981). Between never and always. New England J. Med. 305 1097-1098. 
n = 24: members of Pathology Department, Massachusetts General Hospital. 
(8) KONG, A., BARNETT, G. O., MOSTELLER, F. and YOUTZ, C. (1986). How medical professionals evaluate expressions of probability. New England J. Med. 315 740-744. 
n_a = 140. High probability scale. n_b = 134. Uniform scale. n_0 = 170. Free choice. n_d = 144. Low probability scale. Physicians, medical, non-medical, and auxiliary students and nurses, nationwide. 
(9) LICHTENSTEIN, S. and NEWMAN, J. R. (1967). Empirical scaling of common verbal phrases associated with numerical probabilities. Psychonomic Sciences 9 563-564. 
n = 186: System Development Corporation employees.
(10) LEVINE, J. M. and ELDREDGE, D. (December 1970). The effects of ancillary information upon photo interpreter performance. American Institutes for Research, Institute for Research in Psychobiology, Washington Office, AIR-20131-12/70-FR. 
n = 20: enlisted U.S. Army image interpreters. 
(11) MAPES, R. E. A. (1979). Verbal and numerical estimates of probability in therapeutic contexts. Social Science and Medicine 13A 277-282. 
n_a = 29: physicians given expression "Side effects with chloramphenicol are frequent." n_b = 33: physicians given expression "Side effects with neomycin sulphate are frequent."
(12) NAKAO, M. A. and AXELROD, S. (1983). Numbers are better than words: Verbal specifications of frequency have no place in medicine. Amer. J. Med. 74 1061-1065. 
n_a = 103 physicians. n_b = 106 physicians. Means read from chart. 
(13) REAGAN, R. T., MOSTELLER, F. and YOUTZ, C. (1989). The quantitative meanings of verbal probability expressions. J. Appl. Psychology 74 433-442. 
n = 115: undergraduates in a psychology course, Stanford University. 
(14) REYNA, V. F. (1981). The language of possibility and probability: Effects of negation on meaning. Memory and Cognition 9 642-650. 
n = 41 adult volunteers. 
(15) ROBERTS, D. E. and GUPTA, G. (1987). To the editor. New England J. Med. 316 550. 
n_a = 45 house staff. n_b = 24 attending physicians. 
(16) ROBERTSON, W. 0. (1983). Quantifying the meanings of words. J. Amer. Med. Assoc. 249 2631-2632. 
n_a = 53: Seattle physicians. n_b = 80: graduate students at the University of Washington's School of Business Administration. n_0 = 40: Board of Trustees at the Children's Orthopedic Hospital and Medical Center, Seattle. 
(17) SELVIDGE, J. (1972). Assigning probabilities to rare events. Ph.D. dissertation, Graduate School of Business Administration, George F. Baker Foundation, Harvard Univ. 
Subjects were Harvard Business School students in MBA program. n_a = 59: Estimates made on basis of a statement without context. n_b = 127: Contexts were provided. Also in Mosteller, F. (1977). Assessing unknown numbers: Order of magnitude estimation. In Statistics and Public Policy (W. B. Fairley and F. Mosteller, eds.) 163-184. Addison- Wesley, Reading, Mass. 
(18) SIMPSON, R. H. (1963). Stability in meanings for quantitative terms: A comparison over 20 years. Q. J. Speech 49 146-151. 
1942 study. n_a = 335: 86 high school and 249 college students. 1962 study. n_b = 395 university students. 
(19) TOOGOOD, J. H. (1980). What do we mean by "usually"? Lancet 1 1094. 
n = 51: physicians, nurses, laboratory technologists, secondary school teachers, and engineers. 
(20) MOSTELLER, F. and YOUTZ, C. (1990). Quantifying probabilistic expression. Statistical Science 5 2-34.
estimates from science writers. n = 230: science writers. Varies somewhat from expression to expression, 211-237.
(21) Rohrmann, B. (2007). Verbal qualifiers for rating scales: sociolinguistic considerations and psychometric data. Project report. University of Melbourne. www.rohrmannresearch.net/pdfs/rohrmann-vqs-report.pdf
n = 164; 120 psychology students, 44 subjects from the general population 


---------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: literature_results_intensity.tsv            
---------------------------------------------------------------

// Variable/Column List: 
* study                : study ("krsacok2001", "matthews_etal1978", "rohrmann2007")
* group                : subgroup of subjects (Krsacok 2001: "college_females" vs. "college_males")
* n_subjects           : number of subjects in study (or subgroup of subjects)
* verbal_label         : intensifying adverb (e.g. "extremely", "fairly", "partly")
* mean_rating_original : the mean rating reported in the study
* sd_rating_original   : the standard deviation of ratings reported in the study
* mean_rating          : the mean of rescaled ratings (scale from 0 to 10)
* sd_rating            : the standard deviation of rescaled ratings (scale from 0 to 10)

// Missing data code: 
No missing data.


-----------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: literature_results_probability.tsv            
-----------------------------------------------------------------

// Variable/Column List: 
* verbal_label         : probability expression (e.g. "probable", "very likely", "poor chance")
* percentage           : mean percentage of total referred to by frequency adverb
* measure              : statistical measure used to express the "average percentage" (mean, median)
* study                : study ID (see [A] above)
* n_subjects           : number of subjects in study

// Missing data code: 
No missing data.


-------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: literature_results_quality.tsv            
-------------------------------------------------------------

// Variable/Column List: 
* verbal_label         : quality expression (e.g. "excellent", "fairly good", "poor")
* study_subgroup       : study (subgroup) ID
* n_subjects           : number of subjects in study (subgroup)
* mean_score           : mean score (21-point scale; rescaled to [0,20])
* sd_score             : standard deviation of scores (21-point scale; rescaled to [0,20])

// Missing data code: 
No missing data.


-----------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: literature_results_quantifiers.tsv            
-----------------------------------------------------------------

// Variable/Column List: 
* verbal_label         : quantifier (i.e. "few", "some", "many", "most")
* study_subgroup       : study (subgroup) ID
* n_subjects           : number of subjects in study (subgroup)
* percentage           : mean percentage of total referred to by the quantifier

// Missing data code: 
No missing data.


---------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: results_mosteller_youtz_1990.tsv    
---------------------------------------------------------------

// Variable/Column List: 
* verbal_label         : frequency or probability expression (e.g. "always", "probable", "rarely", "poor chance")
* dimension            : "frequency" vs. "probability"
* mean_percentage      : mean percentage of total referred to by expression
* lower_quartile       : lower quartile of the distribution of percentages across subjects
* median_percentage    : median percentage of total referred to by expression
* upper_quartile       : upper quartile of the distribution of percentages across subjects
* iqr                  : interquartile range as a measure of variation across subjects

// Missing data code: 
No missing data.


----------------------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: survey_rating_scales.tsv
----------------------------------------------------------------------------

// Variable/Column List: 
* study_id          : study id, specific for the current literature survey (e.g. "CLLT 14-1_5")
* journal           : journal in which article appeared
* doi               : digital object identifier (persistent hyperlink for direct access via the journal website)
* year              : year of publication
* variable_measured : a description of the variable that was measured (e.g. "Concreteness and imagery of items")
* role_in_study     : the role of the variable in the research design
   - outcome                (dependent variable)
   - predictor              (independent variable)
   - correlational variable (one of several variables in a correlational analysis)
   - stimulus validation    (ratings used to screen/validate items or materials used in study)
   - sample description     (ratings used to describe sample of subjects/items, not part of analysis)
* multi_item        : whether the rating scale formed part of a multi-item scale (1 yes; 0 no)
* scale_details     : a description of the scale labels provided to informants
   - the number in parentheses refers to the response category (counting from the left to the right)
   - the word/phrase to the right of the number quotes the scale label attached to the category
   - if only numbers are assigned to the categories this is indicated as e.g. "1 to 5"
   - "Likert-type" denotes typical agreement phrases used in Likert scales
   - "Semantic differential scale" refers to scales that are flanked by two antonyms
   - NA denotes cases where the scale design was not ascertainable
* anchors           : descriptors used to indicate the meaning of the response categories
   - each category           (verbal labels for each category)
   - endpoints               (verbal labels only at the endpoints)
   - endpoints and midpoint: (verbal labels at the endpoints and scale midpoint)
   - midpoint                (verbal labels only at the scale midpoint)
   - numbers                 (only numbers for the categories)
   - stars                   (stars were used for the categories)
   - NA                      (scale design was not ascertainable)
* categories        : number of response categories
* analysis          : statistical analysis strategy (multiple entries possible)
   - means                   (conversion to numeric scores)
   - description_categorical (statistics other than the mean/SD; e.g. percentages or medians)
   - orm                     (analysis using an ordinal regression model)
   - binary_regression       (analysis using a series of disconnected binary regression models)
   - nonparametric           (procedures for ranked observations; e.g. Wilcoxon signed-rank tests)
   - NA                      (analysis strategy was not ascertainable)
* dimension         : dimension underlying the rating scale
   - agreement   (typical Likert items, e.g. "strongly agree", ...)
   - intensity   (intensifying adverbs, e.g. "somewhat", "quite", "very")
   - frequency   (frequency expressions, e.g. "sometimes", "usually", "often")
   - probability (probability expressions, e.g. "unlikely", "probable", "very likely")
   - quality     (adjective on the good-bad continuum, e.g. "poor", "good", "excellent")
   - quantifiers (proportional expressions, e.g. "few", "about half", "most")
   - NA          (scale not fully verbalized and/or does not fit one of these categories)

// Missing data code: 
NA


--------------------------
SHARING/ACCESS INFORMATION
--------------------------

// Licenses/Restrictions: See Terms tab.
// Links to publications that cite or use the data: See metadata field Related Publication.
// Recommended citation: See citation generated by repository.


--------------------------
REFERENCES
--------------------------

* Borges, M.A., & B.K. Sawyers. 1974. Common verbal quantifiers: Usage and interpretation. Journal of Experimental Psychology 102, 335–338.

* Krsacok, Stephen J. 2001. Quantification of adverb intensifiers for use in ratings of acceptability, adequacy, and relative goodness. University of Dayton dissertation. https://ecommons.udayton.edu/graduate_theses/3652

* Krug, Manfred & Katrin Sell. 2013. Designing and conducting interviews and questionnaires. In Manfred Krug & Julia Schlüter (eds.), Research methods in language variation and change, 69–98. Cambridge: Cambridge University Press.

* Matthews, J. J., Wright, C. E., Yudowitch, K. L., Geddie, J., & Palmer, R. L. 1978. The perceived favorableness of selected scale anchors and response alternatives. U.S. Army Research Institute for the Behavioral and Social Sciences.

* Mosteller, Frederick & Cleo Youtz. 1990. Quantifying probabilistic expressions. Statistical Science 5(1). 2–34.

* Myers, James H. & W. Gregory Warner. 1968. Semantic properties of selected evaluation adjectives. Journal of Marketing Research 5(4). 409-412.

* Newstead, Stephen E., Paul Pollard & D. Riezebos. 1987. The effect of set size on the interpretation of quantifiers used in rating scales. Applied Ergonomics 18(3), 178–182.

* Rohrmann, Bernd. 2007. Verbal qualifiers for rating scales: sociolinguistic considerations and psychometric data. Project report. University of Melbourne. www.rohrmannresearch.net/pdfs/rohrmann-vqs-report.pdf

* van Tiel, Bob, Michael Franke & Uli Sauerland. 2021. Probabilistic pragmatics explains gradience and focality in natural language quantification. Proceedings of the National Academy of Sciences 118(9). e2005453118.

* VERBI Software. 2021. MAXQDA 2022. Berlin: VERBI Software.

* Vidali, Joseph J. 1975. Context effects on scaled evaluator adjective meaning. Journal of the Market Research Society 17(1). 21-25.

* Wildt, Albert R. & Michael B. Mazis. 1978. Determinants of scale response: Label versus position. Journal of Marketing Research 15(2). 261-267.