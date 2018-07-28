content_string_1 = '<img src="'
content_string_2 = '" alt="" class="responsive-img"><div class="blog-details"><div class="post-title" id="blog-post-'
content_string_3 = '"><a href="#"><h2>'
content_string_4 = '</h2><span>'
content_string_5 = '</span></a></div><div class="post-large-details">'

block_string_1 = '<div class="col s12 m12 l4 blog-post"><div class="thumbnail z-depth-1"><a href="'
block_string_2 = '"><img src="'
block_string_3 = '" alt="" class="responsive-img"></a><div class="blog-details"><div class="post-title" id="blog-post-'
block_string_4 = '"><a href="'
block_string_5 = '</h2><span>'
block_string_6 = '</span></a></div><div class="post-details"><p>'
block_string_7 = '" style="color:#5592CC;">Read More</a></p></div></div></div></div>'

fileCreated = False

while (not fileCreated):
	blog_number = input("Enter the global blog number: ")
	blog_number = blog_number%5

	title = raw_input("Enter the title of the blog: ")
	rel_area = raw_input("Enter the area related to the topic of the blog: ")

	contentFinished = False
	
	content = ""
	block_content = ""

	while (not contentFinished):
		print "Select the appropriate type of content you want to add"
		print "1. Paragraph"
		print "2. Image"
		print "3. Heading"
		print "4. Content Finished"
		content_type = input("Your choice: ")

		if content_type == 1:
			paragraph = raw_input("Enter the Paragraph\n")
			content += "<p>" + paragraph + "</p>" + "\n"
		elif content_type == 2:
			image_link = raw_input("Enter the link of the image: ")
			content += '<img src="' + image_link + '" alt="" class="responsive-img">'
			caption_choice = raw_input("Do you want to add a caption (y/n):")
			if caption_choice == 'y':
				image_caption = raw_input("Enter the caption for the above image: ")
				content += "<center><span>" + image_caption + "</span></center>"
			else:
				continue
			content += "\n"
		elif content_type == 3:
			heading_number = input("Enter the heading number (1 for h1, 2 for h2 and so on..): ")
			heading = raw_input("Enter the heading: ")
			content += "<h" + str(heading_number) + ">" + heading + "</h" + str(heading_number) + ">" + "\n"
		elif content_type == 4:
			contentFinished = True
		else:
			continue

	main_image = raw_input("Enter image link for the main image")
	image_choice = raw_input("Use main image also as thumbnail image (y/n): ")
	
	if image_choice == 'n':
		thumbnail_image = raw_input("Enter image link for the thumbnail image")
	else:
		thumbnail_image = main_image

	filename = raw_input("Enter a desired filename")
	filename = "./blogs/" + filename + ".html"

	content =  "\n" + content_string_1 + main_image + content_string_2 + str(blog_number) + content_string_3 + title + content_string_4 + \
				rel_area + content_string_5 + content + '</div></div>' + "\n"
	
	with open('./blogs/blogtemplate.html', 'r') as myfile:
		template=myfile.read()

	template = template.replace("<!--786-->",content)

	block_para = raw_input("Enter the abstract of your blog: ")

	block_content = "\n" + block_string_1 + filename + block_string_2 + thumbnail_image + block_string_3 + str(blog_number) + \
					block_string_4 + filename + '"><h2>' + title + block_string_5 + rel_area + block_string_6 + block_para + '<br><a href="' + \
					filename + block_string_7 + "\n" + "<!--786-->"


	writeFile = open(filename, "w")
	writeFile.write(template)
	blog_html = open('blog.html', 'r+')
	blog_read = blog_html.read()
	blog_read = blog_read.replace("<!--786-->", block_content)
	blog_html.seek(0)
	blog_html.write(blog_read)
	blog_html.truncate()
	writeFile.close()
	blog_html.close()
	fileCreated = True
	print "\n\n Blog Created \n\n"

	if fileCreated == True:
		extra_file = raw_input("Do you want to create one more blog (y/n) :")
		if extra_file == 'y':
			fileCreated = False

