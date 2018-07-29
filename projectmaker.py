content_string_1 = '<img src="'
content_string_2 = '" alt="" class="responsive-img"><div class="blog-details"><div class="post-title" id="project-post"><a href="#"><h2>'
content_string_3 = '</h2><span>'
content_string_4 = '</span></a></div><div class="post-large-details">'

block_string_1 = '<div class="col s12 m12 l4 blog-post"><div class="thumbnail z-depth-1"><a href="'
block_string_2 = '"><img src="'
block_string_3 = '" alt="" class="responsive-img"></a><div class="blog-details"><div class="post-title" id="project-post"><a href="'
block_string_4 = '"><h2>'
block_string_5 = '</h2><span>'
block_string_6 = '</span></a></div><div class="projjy-post"></div></div></div></div>'

fileCreated = False

while (not fileCreated):
	title = raw_input("Enter the title of the project: ")
	rel_area = raw_input("Enter the area related to the topic of the project: ")

	contentFinished = False
	
	content = ""
	block_content = ""

	while (not contentFinished):
		print "Select the appropriate type of content you want to add"
		print "1. Paragraph"
		print "2. Image"
		print "3. Heading"
		print "4. GitHub Link"
		print "5. Website Link"
		print "6. Research Paper Link"
		print "7. Youtube Video Link"
		print "7. Content Finished"
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
			github_link = raw_input("Enter the GitHub link: ")
			content += '<a href="' + github_link + '"><img src="../assets/social/github-social-logo.png" style="width:64px; height:64px; display:inline;padding:5px;"></a>'
		elif content_type == 5:
			website_link = raw_input("Enter the Website link: ")
			content += '<a href="' + website_link + '"><img src="../assets/social/internet.png" style="width:64px; height:64px; display:inline;padding:5px;"></a>'
		elif content_type == 6:
			paper_link = raw_input("Enter the Research Paper link: ")
			content += '<a href="' + paper_link + '"><img src="../assets/social/document.png" style="width:64px; height:64px; display:inline;padding:5px;"></a>'
		elif content_type == 7:
			youtube_link = raw_input("Enter the Youtube Link: ")
			content += '<a href="' + youtube_link + '"><img src="../assets/social/youtube.png" style="width:64px; height:64px; display:inline;padding:5px;"></a>'
		elif content_type == 8:
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
	filename = "./projects/" + filename + ".html"

	content =  "\n" + content_string_1 + main_image + content_string_2 + title + content_string_3 + \
				rel_area + content_string_4 + content + '</div></div>' + "\n"
	
	with open('./projects/projecttemplate.html', 'r') as myfile:
		template=myfile.read()

	template = template.replace("<!--786-->",content)

	block_content = "\n" + block_string_1 + filename + block_string_2 + thumbnail_image + block_string_3 + filename + \
					block_string_4 + title + block_string_5 + rel_area + block_string_6 + "\n" + "<!--786-->"


	try:
		writeFile = open(filename, "w")
		writeFile.write(template)
		blog_html = open('project.html', 'r+')
		blog_read = blog_html.read()
		blog_read = blog_read.replace("<!--786-->", block_content)
		blog_html.seek(0)
		blog_html.write(blog_read)
		blog_html.truncate()
		writeFile.close()
		blog_html.close()
		fileCreated = True
		print "\n\n Project Created \n\n"
	except:
		print "couldn't make project"

	if fileCreated == True:
		extra_file = raw_input("Do you want to create one more project (y/n) :")
		if extra_file == 'y':
			fileCreated = False

