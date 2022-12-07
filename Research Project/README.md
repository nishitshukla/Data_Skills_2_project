# -*- coding: utf-8 -*-
"""

Abstract

Climate variability and climate change pose enormous pressure on the population,
infrastructure, livelihood, and socio-economic conditions. Evidence of climate change
is already visible in many sectors such as agriculture, water resources, infrastructure, 
ecology, and biodiversity. Moreover, while the problem of climate change is at a global 
scale, its detrimental impacts are often visible at a local scale. This means that many 
of the solutions to combat this impact and safeguard at-risk communities from the worst 
of climate disasters need to be understood from a subnational or local framework. From an 
Indian perspective, frequent floods, erratic rainfall patterns, and intensifying heat waves
are posing grave challenges to India’s agriculture system across the country. With India 
set to become the world’s most populous nation, the high population growth and per capita 
consumption make food security an even greater challenge that needs to be navigated with 
increasing climate risk. This paper aims to explore the effects of irrigation systems in 
countering the effects of droughts and changing rainfall patterns. The analysis conducted 
uses District Level Dataset (DLD) sourced from an open-source agriculture platform 
developed by a joint collaboration between ICRISAT and Cornell Research Institute. Using 
the data, this paper analysis districts in Madhya Pradesh and reaches concludes the 
districts with greater density with irrigation systems fare better during ‘dry’ years than 
districts that don’t have irrigation systems. 


Methodology 

Wheat is the chosen crop for this study due to the large geographical area it covers over 
multiple soil types, this includes the Gangetic plains and Deccan plateau that spans 
over 6 states in the country, allowing for a large sample set of over 150 districts to 
shortlist from, unlike other subregional crops that are grown in small pockets of the 
country. Wheat is also primarily a rabi crop, which means that crops are sown during 
early Sept-Nov after the completion of the monsoon season. This makes it an interesting 
case to study is it allows us to observe the second-order effects of inter-seasonal 
rainfall and allows us to reduce the impact of intra-seasonal rainfall variability. 

Data Source 

The analysis of this paper extensively relies on the District Level Database (DLD) 
developed by ICRISAT and Tata-Cornell Institute for Indian agriculture and allied 
sectors. This data platform provides comprehensive one-stop shop for data on rural 
sector that enables testing of key research hypotheses, identification of relevant 
districts / regions for technology dissemination, promoting rural pro-poor programs / 
development initiatives and identification of relevant representative districts for
micro level assessment.

The platform acts as a link between country-level macro data and household-level micro 
data. The consistent recording and detail at district level makes it a powerful research 
response tool for priority setting and in tracking inter-district and intra-district 
economic changes.

Apart from ICRISAT, the governments official agriculture platform MP Krishi was used to 
source data on district level precipitation levels.                                                                                  

OLS Regression 

This paper uses the Ordinary least squares (OLS) regression as a statistical method to 
estimate the relationship between one or more independent variables and a dependent 
variable; the method estimates the relationship by minimizing the sum of the squares in 
the difference between the observed and predicted values of the dependent variable configured as a straight line. 

In this paper, OLS regression will be discussed in the context of a bivariate model, 
that is, a model in which there is only one independent variable ( X ) predicting a 
dependent variable ( Y ). 

Conclusion

The above OLS regression plot showcases that for every 1% or 0.01 increase in percentage 
gross irrigated area, there is a 23 Kg per ha increase in Wheat yield in districts in 
Madhya Pradesh. The R squared being greater than 0.98 also signifies how a majority of 
the dependent variable is also explained by the independent variable. 

The comparative plot showcases two clear trends. The first trend that comes out is that, 
during dry years, districts with higher percentage irrigated area continuously produce a 
greater yield than its low percentage irrigated area counterparts. 

The second trend that emerged from this analysis is that, with every passing dry year, 
the yield levels for both district groups has increased, barring the years 2001 and 2002.
 
This upward trend may be the result of increased rural development in the state, with 
the Madhya Pradesh government having specifically focussed on accelerating development 
of irrigation systems across most districts over the last decade.

Implication 

The above analysis has clear implications that increasing gross irrigation area 
percentage has a net positive effect on the overall Wheat yield. The following policies 
by the Madhya Pradesh from 2008-09 to 2012-13 showcase what may have led to the success 
increase in overall irrigation: 

1.	Quickly improving power supply for rabi irrigation and rapidly expanding the 
utilization of created canal irrigation potential from major, medium and minor schemes.

2.	The government also began issuing temporary winter season power connections. 
Irrigation demand for power during winter was so high that farmers were willing to 
pay 2.70-3.00/unit for reliable power. The government contracted advance power purchase
for winter months, created a sense of plenty, and began liberally issuing winter-season irrigation connections. 

3.	Madhya Pradesh government spent a total of Rs 36,689 crore on irrigation, far less 
than AP and Maharashtra had done; yet, MP tripled its irrigated area in canal commands 
(from all sources) from 0.80 mha in 2006 to 2.50 mha in 2012-13.

While much of the analysis presented in this paper used data up to 2015-16, it is clear 
that with increasingly erratic monsoons caused by a changing climate, constructing 
irrigation systems could be one of the most effective ways to safeguard farmers from 
droughts and heatwaves. 

Further Research 

This paper is the beginning of a much deeper dive into understanding how irrigation 
exactly effects the wheat yield in Madhya Pradesh. As next steps, this following 
research will provide an analysis of a difference-in-difference regression with 
controls that include education, average household wage, population of districts and 
other variables as control factors. What will also be examined is the differences in 
effects based on different sources of irrigation that exists in Madhya Pradesh. 


"""

