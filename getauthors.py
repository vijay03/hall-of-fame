import csv
import datetime
import dblp
import operator
import pickle
import os

authors = {}

# Load the existing authors if they exist
if os.path.exists("authors.data"):
    authors_file = open("authors.data", 'rb')
    authors = pickle.load(authors_file)

print len(authors)

# Update from the CSV
with open('faculty-affiliations.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        authors[row['name'].strip()] = row['affiliation'].strip()

# Manual additions
authors["David Mazieres"] = "Stanford"
authors["Kai Li"] = "Princeton"
authors["Mike Burrows"] = "Google"
authors["Sylvia Ratnasamy"]= "UC Berkeley"
authors["Martin Abadi"] = "Google"
authors["Sanjay Ghemawat"]  = "Google"
authors["Jay Lepreau"]= " Utah (deceased)"
authors["Chandramohan A. Thekkath"] = "Microsoft Research"
authors["J. Bradley Chen"] = "Google"
authors["Paul Barham"] = "Google"
authors["Edmund B. Nightingale"] = "Microsoft Research"
authors["Chandramohan A. Thekkath"] = "Microsoft"
authors["Kaushik Veeraraghavan"] = "Facebook"

if os.path.exists("authors.data"):
    authors_file.close()

# write new authors file
authors_file = open("authors.data", 'wb')
pickle.dump(authors, authors_file)
authors_file.close()
