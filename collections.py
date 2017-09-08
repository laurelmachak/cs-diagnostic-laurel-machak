#create an array

someMovies = ["The Big Lebowski", "The Room", "Jackie Brown", "Pulp Fiction"]

print(someMovies)

#print the values of the first 3 items from the list
print(someMovies[0:3])
#print the value of the last item of the list
print(someMovies[-2])
#add another movie to the end of the list
someMovies.append("The Simpsons Movie")
#print out value of last item of list
print(someMovies[-1])


#create dictionary

movieDirectors = {"Tarantino" : ["Jackie Brown", "Pulp Fiction", "Kill Bill"], 
"Peter Jackson" : ["The Fellowship of the Ring", "Return of the King"]}

print(movieDirectors)
#print the value assigned to the key 'Tarantino'
print(movieDirectors["Tarantino"])
#b/c the key "Tarantino" value is a list, this will print out the 2nd index of the list assigned
#to the "Tarantino" key
print(movieDirectors["Tarantino"][1])


