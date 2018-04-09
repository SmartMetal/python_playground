formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter	% (True, False, False, True)
print formatter	% (formatter, formatter, formatter, formatter)
#this next print actually ends up putting single quotes 
#on all of the following lines
print formatter % (
	"I had this thing.",
	"that you could type up right.",
	"but it didn't sing.",
	"So I said goodnight."
)