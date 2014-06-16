# Print a formatted price list with a given width

width = input('Please enter width:')

price_width = 10
item_width = width - price_width

header_format = '%-*s%*s'  #- from left and continue to right
item_format = '%-*s%*.2f'

print '=' * width

print header_format % (item_width,'Item',price_width,'Price')

print '-' * width

print item_format % (item_width, 'Apples', price_width, 0.4) 
print item_format % (item_width, 'Pears', price_width, 0.5) 
print item_format % (item_width, 'Cantaloupes', price_width, 1.92) 
print item_format % (item_width, 'Dried Apricots (16 oz.)', price_width, 8) 
print item_format % (item_width, 'Prunes (4 lbs.)', price_width, 12) 

print '=' * width
