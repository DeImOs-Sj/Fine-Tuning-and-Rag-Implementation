import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import csv


# Download NLTK dependencies if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize stopwords and lemmatizer
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Sample data (replace with your actual data)
data = """
The farmer asked about the variety of the plant ?
ASKED ABOUT CONTACT NUMBER OF IARI PUSA DELHI ?
ASKED ABOUT CONTECT NO. OF KVK ?
Farmer asked query on Weather
Plant Protection
Plant Protection
Farmer asked query on Weather
farmer asked about to In how many years is the sandalwood tree ready?
How to register your crop on Kisan Rath Mobile App?
ASKED ABOUT TO CONTACT NUMBER OF KVK, UJWA,DELHI ?
Plant Protection
Plant Protection
Information regarding mushroom production ?
Plant Protection
Plant Protection
Farmer asked query on Weather
Plant Protection
Plant Protection
ASKED ABOUT TO NUTRIENT MANAGEMENT ONION ?
FARMER ASKED ABOUT THE CONTROL OF WEED IN BHINDI ?
Plant Protection
asked about to contact number of iari ?
FOR CALLING KISAAN CALL CENTER
FOR CALLING KISAAN CALL CENTER
FARMER ASKED ABOUT THE SEED ?
testing call
Farmer asked query on Weather
ASKED ME ABOUT ANIMAL DISEASE ?
FARMER ASKED ABOUT THE VARIETY OF PIGEON PEA ?
TELL ME VARIETY OF COTTON ?
FOR CALLING KISAAN CALL CENTER
Farmer asked query on Weather
Plant Protection
ASKED ABOUT TO KISAN CALL CENTER ?
How is dry ginger made?
Plant Protection
ASKED ABOUT TO WEED CONTROL IN BLACK GRAM ?
Farmer asked query on Weather
Government of Uttar Pradesh Food and Civil Supplies Department
Plant Protection
Plant Protection
Plant Protection
Plant Protection
Farmer asked query on Weather
Farmer asked query on Weather
FOR CALLING KISAAN CALL CENTER
FOR CALLING KISAAN CALL CENTER
Plant Protection
Plant Protection
Farmer asked query on Weather
Plant Protection
ASKED ABOUT TO MANDI PRICE OF DELHI ?
ASKED ABOUT CONTECT NO. OF KVK ?
FOR CALLING KISAAN CALL CENTER
ASKED ABOUT CONTECT NO. OF PUSA ?
Plant Protection
FARMER ASKED ABOUT THE BREAD OF GIROLANDO ?
FOR CALLING KISAAN CALL CENTER
ASKED ME ABOUT MANDI PRICE OF WHEAT ?
ASKED ABOUT CONTROL OF FLOWER DROPPING IN POMGRANATE ?
ASKED ABOUT TO CONTROL OF FLOWER DROPING IN MOSAMBI ?
ASKED ABOUT TO NUTRIENT MANAGEMENT ?
FOR CALLING KISAAN CALL CENTER
ASKED ABOUT TO KISAN CALL CENTER ?
Plant Protection
ASKED ABOUT TO MICRO NUTRIENT MANAGEMENT ?
FOR CALLING KISAAN CALL CENTER
Plant Protection
FARMER ASKED ABOUT THE CONTROL OF WEED I
FOR CALLING KISAAN CALL CENTER
Plant Protection
FOR CALLING KISAAN CALL CENTER
ASKED ABOUT TO MANDI RATE IN WHEAT ?
Plant Protection
TELL ME ABOUT TAKING SOIL SAMPLE ?
FARMER ASKED QUERY ON PUSA CONTACT NO
ASKED ABOUT TO CONTROL OF FLOWER DROPING IN DATEPALM ?
Farmer asked query on Weather
Farmer asked query on Weather
Farmer asked query on Weather
Tell me contact number of National and Regional Organic Farming Centres Ghaziabad ?
FOR CALLING KISAAN CALL CENTER
ASKED ABOUT SOWING TIME OF GREENGRAM ?
ASKED ABOUT TO ANIMAL CARE HELPLINE NUMBER 24 HOURS ?
Farmer asked query on Weather
FOR CALLING KISAAN CALL CENTER
Plant Protection
Plant Protection
Plant Protection
Water Management
Plant Protection
Plant Protection
Farmer asked query on Weather
ASKED ABOUT TO VARIETY OF SORGHUM ?
ASKED ABOUT TO MANDI PRICE OF WHEAT ?
Farmer asked query on Weather
farmer asked about to Kisan Saathi Portal Information ?
farmer asked about to Kisan Saathi Portal Information ?
Plant Protection
Plant Protection
ASKED ABOUT CONTECT NO. OF agmarknet ?
Asked about to contact number of najafgarh mandi ?
FOR CALLING KISAAN CALL CENTER
Krishi Vigyan Kendra, Ujwa, Delhi
ask about variety of Rajma and arhar ?
Farmer asked query on Weather
TEST CALL
Plant Protection
Plant Protection
ASKED ABOUT TO NUTRIENT MANAGEMENT IN ?
ASKED ABOUT ANIMAL HUSBANDRY CONTACT NUMBER DELHI ?
FARMER ASKED ABOUT THE SEED AND PLANTING MATERIAL ?
Plant Protection
Farmer asked query on Weather
Plant Protection
FARMER ASKED ANIMAL DEPTT. INFO ?
Plant Protection
Plant Protection
TELL ME ANIMAL HUSBANDRY CONTACT NUMBER KARNAL ?
FOR CALLING KISAAN CALL CENTER
ASKED ABOUT TO VARIETY OF BHINDI ?
FOR CALLING KISAAN CALL CENTER
Plant Protection
ask about helpline number animal husbandry ?
Plant Protection
ASKED ABOUT TO NUTRIENT MANAGEMENT IN ONION ?
farmer asked about to quantity of seeds for sowing jawar ?
FARMER ASKED ABOUT THE WHICH FRUIT PLANT ARE SUTIABLE FOR INDOOR ?
ASKED ABOUT NUTRIENT MANAGEMENT ?
FARMER ASKED ABOUT THE RAJ-KISAN SATHI PORTAL ?
FARMER ASKED FOREST DEPARTMENT CONTACT NUMBER ?
FOR CALLING KISAAN CALL CENTER
Farmer asked query on Weather
ASKED ABOUT KISAN VIKASH PATAR ?
Plant Protection
Plant Protection
Plant Protection
Farmer asked query on Weather
Farmer asked query on Weather
FARMER ASKED ABOUT ICAR-Indian Grassland and Fodder Research Institute PHONE NO. ?
Farmer asked query on Weather
Plant Protection
farmer asked about to agriculture drone license information ?
ask about mushroom cultivation ?
ASKED ABOUT NUTRIENT MANAGEMENT ?
Plant Protection
FARMER ASKED ABOUT THE CONTACT NUMBER OF ANIMAL DEPARTMENT ?
Plant Protection
FOR CALLING KISAAN CALL CENTER
asked about contact number of pusa seed unit
Plant Protection
TELL ME VARIETY OF PAPAYA
Water Management
FOR CALLING KISAAN CALL CENTER
ASKED ABOUT TO STOP SPROUTING IN ONION?
Farmer asked query on Weather
FOR CALLING KISAAN CALL CENTER
ASKED ABOUT TO KISAN CALL CENTER ?
ASKED ME ABOUT GREEN GRAM VARIETY ?
Water Management
FOR CALLING KISAAN CALL CENTER
farmer asked about to land and field preparation ?
ask about disease management in goat
ASKED ABOUT VARITY OF BASMATI RICE ?
FARMER ASKED MANDI NUMBER ?
FARMER ASKED ABOUT THE CONTACT NUMBER OF AGRICULTURE COMMISSIONER IN ANDHRA PRADESH STATE ?
farmer asked about to kisan rath information ?
ASKED ABOUT TO WEED CONTROL IN BLACK GRAM ?
ASKED ABOUT ANIMAL HUSBANDRY CONTACT NUMBER DELHI ?
FARMER ASKED ABOUT THE VARIETY OF PADDY ?
FARMER ASKED ABOUT THE TRAINING AND EXPOSURE VISITS ?
FOR CALLING KISAAN CALL CENTER
Plant Protection
Farmer asked query on Weather
Plant Protection
FARMER ASKED KVK CONTACT NUMBER ?
ASKED ABOUT TO MANDI PRICE OF WHEAT ?
Plant Protection
FARMER ASKED ME VARIETY OF PADDY ?
Farmer asked query on Weather
FOR CALLING KISAAN CALL CENTER
FARMER ASKED ABOUT TO VARIETY IN JOWAR ?
information regarding test call?
FOR CALLING KISAAN CALL CENTER
asked about nutrient management in citrus
Farmer asked query on Weather
When to plant zinnia
Plant Protection
Farmer asked query on Weather
ASKED ABOUT TO NUTRIENT MANAGEMENT IN BOTTLE GOURD ?
ASKED ABOUT TO MICRO NUTRIENT MANAGEMENT
Plant Protection
FOR CALLING KISAAN CALL CENTER
Plant Protection
ASKED ABOUT TO ANIMAL CARE HELPLINE NUMBER 24 HOURS ?
Farmer asked query on Weather
information about nutrient application for growth in coriander
Plant Protection
What comes in food processing?
Farmer asked query on Weather
FOR CALLING KISAAN CALL CENTER
ASKED ABOUT TO KISAN CALL CENTER ?
Farmer asked query on Weather
Plant Protection
ASKED ABOUT TO NUTRIENT MANAGEMENT IN ONION ?
Information about beneficiary status of PM Kisan samman nidhi scheme..?
FOR CALLING KISAAN CALL CENTER
Farmer asked query on Weather
call center cooming calls
ASKED ABOUT TO KISAN CREDIT CARD INFORMATION ?
ASKED ABOUT TO SEED TREATMENT OF GREEN GRAM ?
farmerasked about animal fair info ?
ASKED ABOUT TO WATER MANAGEMENT IN ORANGE ?
Plant Protection
ASKED ABOUT CONTACT NUMBER OF IARI PUSA DELHI ?
ASKED ABOUT TO KISAN CREDIT CARD INFORMATION ?
FARMER ASKED ABOUT THE TAKE A SOIL SAMPLE ?
Plant Protection
FARMER ASKED MATURITY PERIOD INFORMATION ?
Plant Protection
FARMER ASKED ABOUT THE CONTACT NUMBER OF ANIMAL HUSBANDRY ?
FARMER ASKED ABOUT THE PMKVY TRAINING CENTER ?
"
ASKED ABOUT CONTECT NO. OF SOIL TESTING LAB ?"
Plant Protection
FARMER ASKED ABOUT THE MANDI RATE OF MUSTARD ?
ASKED ABOUT TO WEED CONTROL IN GROUNDNUT ?
Plant Protection
ASKED ABOUT NUTRIENT MANAGEMENT ?
FARMER ASKED ABOUT THE CONTROL OF DISEASE IN RIBBED GOURD ?
Farmer asked query on Weather
ASKED ABOUT TO MANDI PRICE OF WHEAT ?
Farmer asked query on Weather
Farmer asked query on Weather
ASKED ABOUT TO SOWING TIME OF FRENCH BEAN ?
Farmer asked query on Weather
Farmer asked query on Weather
what should be planted in mango plant
Farmer asked query on Mandi details
farmer asked about to organic vegetable ?
ASKED ABOUT TO SOWING TIME OF OKRA ?
FOR CALLING KISAAN CALL CENTER
Farmer asked query on Weather
ASKED ABOUT CONTACT NUMBER OF IARI PUSA DELHI ?
Plant Protection
Plant Protection
FARMER ASKED ABOUT THE NUTRIENT MANAGEMENT IN BOTTLE GOURD IN POT ?
Plant Protection
Farmer asked price detail of Wheat in Anoop Shahar mandi.
farmer asked about to seed rate in papaya ?
farmer asked about to Where can I do goat farming training ?
ask about Kisan Raja system ?
Plant Protection
ASKED ABOUT TO CONTROL OF FLOWER DROPING IN MANGO ?
FARMER ASKED CONTACT NUMBER ?
ASKED ABOUT TO VARIETY OF BAJRA ?
FOR CALLING KISAAN CALL CENTER
FOR CALLING KISAAN CALL CENTER
Which crop to plant at this time ?
ASKED ABOUT TO CONTACT NUMBER OF IARI PUSA DELHI ?
Farmer asked query on Weather
Plant Protection
Plant Protection
Plant Protection
Farmer asked query on Weather
Plant Protection
TELL ME VARIETY OF MOONG
ASKED ABOUT NUTRIENT MANAGEMENT ?
information about sowing time in capsicum
farmer asked about to waste decomposer ?
Plant Protection
Farmer asked query on Weather
FOR CALLING KISAAN CALL CENTER
TEST CALL
Farmer asked query on Weather
FOR CALLING KISAAN CALL CENTER
FOR CALLING KISAAN CALL CENTER
FARMER ASKED ABOUT TO VEGETABLES INFORMATION ?
ASKED ABOUT TO CONTROL OF FLOWER DROPING IN CITRUS ?
Farmer asked query on Weather
FARMER ASKED CARI CONTACT NUMBER ?
ASKED ABOUT TO CONTROL OF FLOWER DROPING IN ORANGE ?
FOR CALLING KISAAN CALL CENTER
FARMER ASKED ABOUT THE CONTACT NUMBER OF PUSA ?
Benefits of Dhanzyme Gold
FOR CALLING KISAAN CALL CENTER
FARMER ASKED MSP RATE IN WHEAT ?
ASKED ABOUT TO VERITIES OF SORGHUM ?
The farmer has given the price of wheat today ?
In how many days does gourd seed germinate?
ASKED ABOUT TO CONTACT YOUR BLOCK NODAL OFFICER ?
FARMER ASKED ABOUT KRISHI UPAJ MANDI CONTACT NUMBER ?
FARMER ASKED ABOUT TO MANDI RATE IN WHEAT ?
Farmer asked query on Weather
ASKED ABOUT TO FLOWER PROMOTING IN VEGETABLES ?
FARMER ASKED ABOUT ELECTRIC MOTOR ?
TELL ME ABOUT TAKING SOIL SAMPLE ?
Farmer asked query on Weather
ASKED ABOUT TO KISAN CREDIT CARD ?
SEED RATE
Plant Protection
ASKED ABOUT TO VAREITY OF MOONG BEAN ?
FOR CALLING KISAAN CALL CENTER
FARMER ASKED KVK CONTACT NUMBER ?
ASKED ABOUT TO NUTRIENT MANAGEMENT IN ?
Farmer asked query on Mandi details
Thank you for calling Kisan Call Center
farmer asked about to animal insurance scheme delhi ncr information ?
ASKED ABOUT TO KISAN CREDIT CARD INFORMATION ?
farmer asked about to land and field preparation ?
Krishi Vigyan Kendra,Post Box-28,Sonipat, Haryana"""

# Step 1: Convert to lowercase
data = data.lower()

# Step 2: Remove special characters and punctuation
data = re.sub(r'[^\w\s]', '', data)

# Step 3: Tokenize the text
tokens = word_tokenize(data)

# Step 4: Remove stopwords
filtered_tokens = [word for word in tokens if word not in stop_words]

# Step 5: Lemmatize the tokens
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

# Step 6: Join the tokens back into cleaned text
cleaned_data = ' '.join(lemmatized_tokens)

with open('cleaned_queries.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Query'])  # Writing header
    for query in cleaned_data:
        writer.writerow([query])


print(cleaned_data)
