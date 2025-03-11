from PIL import Image
import matplotlib.pyplot as pyplot
import io

# Data
console_sales = {
    2020: (('Switch', 'Xbox', 'Playstation'), (1.549, 0, 0)),
    2021: (('Switch', 'Xbox', 'Playstation'), (1.544, 0.325, 0.653)),
    2022: (('Switch', 'Xbox', 'Playstation'), (1.328, 0.605, 0.708)),
    2023: (('Switch', 'Xbox', 'Playstation'), (1.140, 0.456, 1.257))
}

# Plot
images = []
for year, data in console_sales.items():
    fig = plt.figure(figsize = (6,5))
    #testing plt.plot()
    #testing plt.bar(['a', 'b', 'c'],[5,1,10])
    companies, sales = data
    plt.bar(
        companies,
        sales,
        color = ['red', 'green', 'blue'])
    plt.title(f'Console sales in {year}')
    plt.ylabel('Sales in millions') 
    #testing plt.show()
    #testing plt.savefig('test.png')
    buffer = io.BytesIO()
    plt.savefig(buffer, format = 'png')
    image = Image.open(buffer)
    image.append(image)

# Create the animation
images[0].save(
    fp = 'animated_graph.gif', 
    append_images = images[1:],
    save_all = True,
    duration = 500,
    loop = 0)
