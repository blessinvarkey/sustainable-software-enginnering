# Sustainable Software Enginnering

### Contents
- [Roles, Responsibilities and Sustainability](roles-and-sustainability.md)
- [Power Consumption](power-consumption.md)
- [Big-O-Notation](big-o-notation.md)

- Everything we do with ICT causes some kind of emission

‘..Sustainable development meets the needs of the present without compromising the ability of future generations to meet their own needs’ - Brundtland report 

About three weeks ago, HPI launched a course on Sustainable Software Engineering. While sustainable software practices aren’t new - courtesy of my engineering team - this course does cover quite a few topics which can be useful for someone new to sustainable or green software/coding. 

## CO2 consumption by ICT 
__Bitcoin/Deep Learning:__ Some of the algorithms (Bitcoin note) have massive energy and CO2 footprint
ebook reader: Getting an ebook does reduce cutting trees and ink. However, a 200g ebook requires about 15 kg of raw materials (e.g. rare earth metal), 300L water, and 170 kg of CO2. which means, it won’t be ecologically beneficial until you read 30-60 books on your ebook reader. 
__Emails:__ 1 MB Email is equivalent to 20g of CO2. So if you write 20 emails on 365 days its equivalent to a car travelling 1000 km. 
Web Search: A web search is equivalent to 3.5 Wh ( ≈ 1 g of CO2). 2-3 web searches per day ≈ 10kg of CO2 per year. 
Average per capita consumption ≈ 1,400km by car

__But why should I care?__
Paris agreement states that the global average temperature should be well below 2*C by 2100 (above pre-industrial levels) to aim to limit the increase to 1.5°C
Global electricity demand caused by ICT: Some say its 1%, others 5 or 10%. 2
The average footprint of the average European citizen is currently  ≈ 10t CO2 p.a.
Data centers could consume 28% of total energy consumption (est. 11%, best: 4%). “In the worst case scenario ICT electricity usage could contribute upto 23% of the globally released greenhouse gas emission in 2030.”

## Potential for ICT & Digitization (assumptions)
- Intelligent Building Management Systems & Smart Grids with intelligent software and good hardware components can save CO2 (20-30% energy reduction) using ICT  
- Working from home/Remote work: Reduces 15-17% of fossil fuel consumption
Digitalizing patient records can help Health sector 

## What can I do? 
Whether you are participant of an engineering team as a leader, architect, developer or a stakeholder, there are multiple ways of making contribution towards sustainable software engineering.
- Agile development 
- DevOps
- Cloud Infrastruture 
- Mobile devices
- Hyperscalre cloud providers
- Content Delivery Networks
- Defining non-functional requirements


## Desinging energy efficient IT-architecture: 
- Breaking up services by resource scaling factors (potentially microservices)
- Ensuring services can scale up and down
- Collaborate for efficient bin packing
- Bin Packing:
    - Pack virtual machines or containers on physical hardware to maximize utilizatoin
    - Pack items of different sizes into a finite number of bins of a fixed given capacity while minimizing number of bins used
    - Smaller/more fine granular items lead to less fragmentation and more optimal solutions
    - Delegating bin packing decisions to lower levels can increase overall efficiency
    - Requires collaboration of all involved stakeholders
- Architects: Service Architecture (e.g. monoliths vs microservices)
Developers: Packaging Solutions (serverless, containers, VMs)
    - Infrastructure Providers: Optimize hardware utilization
- Scaling: 
    - Compute (volatile memory)
    - Storage (persistent)
    - Network
    - Demanding sustainability by leveraging existing forms of functional and non-functional requirements (performance, user experience)


## The GREENSOFT Model: An exisiting green computing approach 

Green Software Engineering was the attempt to apply these "green" principles known from hardware products also on software products, software development processes and their underlying software process models.  
The first main goal of the project was to to design a conceptual reference model supporting IT professionals and software users in the sustainable development and usage of software. 
The second main goal was to develop a software toolbox called "Sustainable Software Support Center" (S3C) that assists IT professionals in realizing sustainable, resource-friendly software products.
![](images/greensoftmodel.png)

### References
1. Sustainable Software Enginnering, Mathias Renner, Ferdinand Mutsch, Johannes Rudolph, Robin Lamberti 


### Reference Material/ Courses
1. [Sustainable Software Engineering](https://open.hpi.de/courses/sustainablesoftware2022?locale=en) 
2. [The Principles of Sustainable Software Engineering](https://docs.microsoft.com/en-us/learn/modules/sustainable-software-engineering-overview/?ocid=AID3038246&WT.mc_id=green-9537-cxa)


### Articles/Blogs/Books
1. [The Social Responsibility of Software Development](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7888390)
2. [Branch](https://branch.climateaction.tech/issues/)
3. [Catalog of Energy Patterns for Mobile Applications](https://arxiv.org/pdf/1901.03302.pdf)

### Libraries/Packages
Track and predict the energy consumption and carbon footprint of training deep learning models.    
1. [Code Carbon](https://codecarbon.io) (A Python package)    
2. [Carbon Tracker](https://github.com/lfwa/carbontracker) (package)   

### Websites for Sustainability Testing
- [Website Carbon](https://www.websitecarbon.com) 





### Contribute Your Favourites

Please share your links sustainable software development resources (courses, packages, books, articles, videos, podcasts) by adding them to this list. Just make a pull request!


### License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)