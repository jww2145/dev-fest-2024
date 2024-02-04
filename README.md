# Environmental-Politics-by-the-Numbers

## Description

The aim of this project is to explore the voting trends of US Politicians when it comes to environmental politics. We know that in the current state of US Affairs, voting is very bipartisan; however, we also believe that there could be some novel information that helps consistuents make an informed decision when going to the polls. Thus, we wanted to try and provide useful and tangible information through a variety of data visualization techniques. 

Our approach to this project was two pronged: before we could analyze any data we needed to obtain said data. Naturally, our first plan of attack was to scrape the 'https://scorecard.lcv.org/' website for both house and senate votes on environmental bills. Conveniently, the website provides an option for us to export data as CSV, so we used a **python** script with the BeautifulSoup and Selenium libraries to handle that for us. Our csvs ended up being too big to push into this github repository, but we have included both python scripts for a user to run. 

The second prong was front-end. Because svelte is lightweight and highly modular with it's components structure, we decided it would be the best choice for this sort of project where we needed to organize different charts and features. We were able to successfully build and output a server file; however, when it came time to deploy it on Heroku, we sadly could not figure it out (yet). 

While we are proud of our achievements in the past 24 hours, we hope in the future to fully flesh out the House of Representative section and incorporate some Machine Learning. In fact, we have built both a voting model to simulate votes and a NLP model to extract features from bills; however, we were unable to use it for this hackathon. 

## Installing and Running

If you want to run the app locally, you can! We have uploaded our csvs and json objects using gist.github.com, so our JavaScript fetches do not need access to a server or external API. To run our app, follow the standard practice of 

1. Cloning or Forking the Repo
2. Cd-ing into the 'myapp' folder
3. npm install
4. npm run dev

If, however, you want to build your own csv, we have included the .py scripts under the **./data-exploration/csv-files** folder. 

## How to Use The Project

We tried our best to make our project super easy to use. It is a static webpage that you can scroll through. 

For the interactive Senate and Congress map, simply click on the image (for senators) or click on the district (for congressmen)! For the line graph, you can filter through by issue via the dropdown menu. 

## Credit 

1. [Katie Marriner](https://github.com/katiemarriner) for providing useful tips and tricks about svelte, d3.json and topojson - all tools we have used in this hackathon! 
2. [Jeremiah Kimelman](https://gist.github.com/jeremiak) for providing the congressional district map, which we have only slightly altered 
3. [Herb Susmann](https://github.com/herbps10) for providing the current Senate Map
4. [The @unitedstates project](https://theunitedstates.io/) for providing images for the senators (and all the other information!) 
