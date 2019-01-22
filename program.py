from easyfacenet.simple import facenet

images = ['assets/img1.jpg', 'assets/img2.jpg', 'assets/img3.jpg']

aligned = facenet.align_face(images)
comparisons = facenet.compare(aligned)

print("Is image 1 and 2 similar? ", bool(comparisons[0][1]))
print("Is image 1 and 3 similar? ", bool(comparisons[0][2]))