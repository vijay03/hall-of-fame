# -*- coding: UTF-8 -*-

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
authors["Gregory R. Ganger"] = "CMU"
authors["Lidong Zhou"] = "MSR Asia"
authors["Robert Tappan Morris"] = "MIT"
authors["Haibo Chen 0001"] = "Shanghai Jiao Tong University"
authors["Brian N. Bershad"] = "Google"
authors["Xi Wang 0005"] = "University of Washington Seattle"
authors["Shan Lu 0001"] = "University of Chicago"
authors["Miguel Castro 0001"] = "Microsoft Research"
authors["Michael Dahlin"] = "Google"
authors["Amin Vahdat"]= "Google"
authors["Jon Howell"] = "VMware Research"
authors["Steven D. Gribble"] = "Google"
authors["Irene Zhang"] = "Microsoft Research"
authors["Allen Clement"] = "DFINITY"
authors["Sanidhya Kashyap"] = "EPFL"
authors["Gerald J. Popek"] = "UCLA (deceased)"
authors["Paul Barham 0001"] ="Google"
authors["Rong Chen 0001"] = "Shanghai Jiao Tong University"
authors["Michael Burrows"] = "Google"
authors["Michael Kaminsky"] = "BrdgAI and CMU"
authors["Dan R. K. Ports"] = "Microsoft Research"
authors["Antony I. T. Rowstron"] = "Microsoft Research"
authors["Srinath T. V. Setty"] = "Microsoft Research"
authors["Marvin Theimer"] = "Amazon Web Services"
authors["Aditya Akella"] = "University of Texas at Austin"
authors["Jinyang Li 0001"] = "NYU"
authors["Peng Huang 0005"] = "John Hopkins"
authors[u"Martín Abadi"] = "Google"
authors["Marcos K. Aguilera"] = "VMware Research"
authors["Sebastian Angel"] = "Penn State"
authors["Ricardo Bianchini"] = "Microsoft Research"
authors["Tej Chajed"] = "MIT"
authors["Byung-Gon Chun"] = "Seoul National University"
authors["Heming Cui"] = "University of Hong Kong"
authors["Chris Hawblitzel"] = "Microsoft Research"
authors["Dejan Kostic"] = "KTH Royal Institute of Technology"
authors["Philip Alexander Levis"] = "Stanford"
authors["Jacob R. Lorch"] = "Microsoft Research"
authors["Yu Luo"] = "Facebook"
authors["Changwoo Min"] = "Virginia Tech"
authors["Madanlal Musuvathi"] = "Microsoft Research"
authors["Vijayan Prabhakaran"] = "Databricks"
authors["Kirk Rodrigues"] = "University of Toronto"
authors["Michael D. Schroeder"] = "Microsoft Research"
authors["Yee Jiun Song"] = "Instabase"
authors["Chandramohan A. Thekkath"] = "Microsoft Research"
authors["Shivaram Venkataraman"] = "University of Wisconsin-Madison"
authors["Yuan Yu"] = "Microsoft"
authors["Guoqing Harry Xu"] = "UCLA"

if os.path.exists("authors.data"):
    authors_file.close()

# write new authors file
authors_file = open("authors.data", 'wb')
pickle.dump(authors, authors_file)
authors_file.close()
