<script>
  import * as d3 from 'd3'
  import { onMount } from 'svelte'

  export const prerender = true;


  onMount(() => {
    // set the dimensions and margins of the graph
  var margin = {top: 10, right: 100, bottom: 30, left: 30},
      width = 460 - margin.left - margin.right,
      height = 400 - margin.top - margin.bottom;

  // append the svg object to the body of the page
  var svg = d3.select("#my_dataviz")
    .append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
    .append("g")
      .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

    
    d3.csv("https://gist.githubusercontent.com/jww2145/412d865cd12317e9e8486194cd23c229/raw/386bf6fcc73542d9883159e0fb52264cc5139eec/senate-issues.csv").then(function(data) {
      var allGroup = ["public right to know", "forests", "water", "lands", "climate", "justice and democracy", "public lands", "judiciary", "transportation", "drilling", "oceans", "wildlife", "toxics", "agriculture", "other", "air", "environmental justice", "energy"]

      const dataReady = allGroup.map(function(grpName) { 
        return{
          name: grpName,
          values: data.map(function(d){
            return {time: d.time, value: +d[grpName]}
          })
        };
      });


      var myColor = d3.scaleOrdinal()
        .domain(allGroup)
        .range(d3.schemeSet2);
      
      var x = d3.scaleLinear()
        .domain([1971,2023])
        .range([0,width]);
      
      svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x))
      
      var y = d3.scaleLinear()
        .domain([1,0])
        .range([0,height]);
          // Add the lines
    const line = d3.line()
      .x(d => x(+d.time))
      .y(d => y(+d.value))

      svg.selectAll('myLines')
        .data(dataReady)
        .enter()
        .append("path")
        .attr("d", function(d){return line(d.values)})
        .attr("stroke", function(d){ return myColor(d.name) })
        .style("stroke-width", 4)
        .style("fill", "none")

        svg
      // First we need to enter in a group
        .selectAll("myDots")
        .data(dataReady)
        .enter()
          .append('g')
          .style("fill", function(d){ return myColor(d.name) })
        // Second we need to enter in the 'values' part of this group
        .selectAll("myPoints")
        .data(function(d){ return d.values })
        .enter()
        .append("circle")
          .attr("cx", function(d) { return x(d.time) } )
          .attr("cy", function(d) { return y(d.value) } )
          .attr("r", 5)
          .attr("stroke", "white")
        
        svg
          .selectAll("myLabels")
          .data(dataReady)
          .enter()
            .append('g')
            .append("text")
              .datum(function(d) { return {name: d.name, value: d.values[d.values.length - 1]}; }) // keep only the last value of each time series
              .attr("transform", function(d) { return "translate(" + x(d.value.time) + "," + y(d.value.value) + ")"; }) // Put the text at the position of the last point
              .attr("x", 12) // shift the text a bit more right
              .text(function(d) { return d.name; })
              .style("fill", function(d){ return myColor(d.name) })
              .style("font-size", 15)

    })
  })

  function buildChart(data){
    var allGroup = Object.keys(data['1971'])

    var dataReady = allGroup.map( function(grpName){
      return{
        name: grpName,
        values: data.map
      }
    })
  }
</script>

<div id="my_dataviz"></div>
