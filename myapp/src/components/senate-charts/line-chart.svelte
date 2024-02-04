<script>
  import { onMount } from "svelte";
  import * as d3 from "d3";

<<<<<<< HEAD
  export const prerender = true;

=======
>>>>>>> cf2458e (added a dropdown for relevance graph)
  let svg;
  let issues;
  let x;
  let y;
  let myLine;

  onMount(() => {
<<<<<<< HEAD
    const margin = { top: 60, right: 80, bottom: 30, left: 50 };
    const width = 1000 - margin.left - margin.right;
    const height = 500 - margin.top - margin.bottom;

    svg = d3.select("#line-chart");

    svg.append("text")
      .attr("x", (width / 2) + margin.left) // Position at the center of the graph width-wise
      .attr("y", margin.top / 2) // Position slightly above the graph
      .attr("text-anchor", "middle") // Ensure the text is centered at its position
      .style("font-size", "24px") // Set the font size of the title
      .style("font-family", "Georgia, serif") // Optional: Set the font family of the title
      .text("Trending Topics"); // Set the text of the title

    const g = svg
      .append("g")
      .attr("transform", `translate(${margin.left},${margin.top})`);

=======
    const margin = { top: 20, right: 80, bottom: 30, left: 50 };
    const width = 1000 - margin.left - margin.right;
    const height = 500 - margin.top - margin.bottom;

    svg = d3.select("svg");

    const g = svg
      .append("g")
      .attr("transform", `translate(${margin.left},${margin.top})`);

>>>>>>> cf2458e (added a dropdown for relevance graph)
    x = d3.scaleLinear().domain([1971, 2023]).range([0, width]);
    y = d3.scaleLinear().domain([1, 0]).range([height, 0]);

    myLine = g.append("path");
<<<<<<< HEAD


    const line = d3
      .line()
      .curve(d3.curveBasis)
      .x((d) => x(d.time))
      .y((d) => y(d.rate));

    d3.csv("https://gist.githubusercontent.com/jww2145/412d865cd12317e9e8486194cd23c229/raw/386bf6fcc73542d9883159e0fb52264cc5139eec/senate-issues.csv").then(function(data){
      issues = data.columns.slice(1).map((id) => {
          return {
            id: id,
            values: data.map((d) => {
              return {
                time: +d.time,  // Convert to number
                rate: +d[id],   // Convert to number
              };
            }),
          };
        });


        x.domain(d3.extent(data, (d) => d.time));

        y.domain([
          d3.min(issues, (c) => d3.min(c.values, (d) => d.rate)),
          d3.max(issues, (c) => d3.max(c.values, (d) => d.rate)),
        ]);

        g.append("g")
          .attr("class", "axis axis--x")
          .attr("transform", `translate(0,${height})`)
          .call(d3.axisBottom(x).tickFormat(d3.format("d")));
=======

    const clip = svg
      .append("svg:clipPath")
      .attr("id", "clip")
      .append("svg:rect")
      .attr("x", 0)
      .attr("y", 0)
      .attr("width", width)
      .attr("height", height);

    const line = d3
      .line()
      .curve(d3.curveBasis)
      .x((d) => x(d.time))
      .y((d) => y(d.rate));

    d3.csv("https://gist.githubusercontent.com/jww2145/412d865cd12317e9e8486194cd23c229/raw/386bf6fcc73542d9883159e0fb52264cc5139eec/senate-issues.csv").then(function(data){
      issues = data.columns.slice(1).map((id) => {
          return {
            id: id,
            values: data.map((d) => {
              return {
                time: +d.time,  // Convert to number
                rate: +d[id],   // Convert to number
              };
            }),
          };
        });


        x.domain(d3.extent(data, (d) => d.time));

        y.domain([
          d3.min(issues, (c) => d3.min(c.values, (d) => d.rate)),
          d3.max(issues, (c) => d3.max(c.values, (d) => d.rate)),
        ]);

        g.append("g")
          .attr("class", "axis axis--x")
          .attr("transform", `translate(0,${height})`)
          .call(d3.axisBottom(x));
>>>>>>> cf2458e (added a dropdown for relevance graph)

        g.append("g")
          .attr("class", "axis axis--y")
          .call(d3.axisLeft(y))
          .append("text")
          .attr("transform", "rotate(-90)")
          .attr("y", 6)
          .attr("dy", "0.71em")
          .attr("fill", "#000")
<<<<<<< HEAD
          .text("Percent");

        // Horizontal grid lines
        g.append("g")
          .attr("class", "grid")
          .style("stroke-width", ".5px")
          .style("stroke-opacity", .25)
          .call(d3.axisLeft(y).tickSize(-width).tickFormat(''));

        // Vertical grid lines
        g.append("g")
          .attr("class", "grid")
          .style("stroke-width", ".5px")
          .style("stroke-opacity", .25)
          .attr("transform", `translate(0,${height})`)
          .call(d3.axisBottom(x).tickSize(-height).tickFormat(''));


=======
          .text("Count");
>>>>>>> cf2458e (added a dropdown for relevance graph)

        const selector = d3.select("#issue_list").append("select");

        const labels = selector
          .selectAll("option")
          .data(issues)
          .enter()
          .append("option")
          .attr("value", (_, i) => i)
          .text((d) => d.id);

        const menu = d3.select("#issue_list select").on("change", redraw);

        redraw();

        function redraw() {
          const series = menu.property("value");
          const adata = issues[series];

          myLine.datum(adata.values)
            .attr("d", line)
            .attr("stroke", "teal")
            .attr("fill", "none");
        }
      }
    );
    });
</script>

<style>
<<<<<<< HEAD
  .parent{
    display: flex;
    flex-direction: row;
    align-content: center;
    align-items: center;
  }

  .left-child{
    padding:2%;
  }

</style>

<body>
  <div class = 'parent'>
    <div class='left-child'>
      <svg id = "line-chart" width="1000" height="500"></svg>
    </div>
   <div class ='right-child'>
    <div id="issue_list"></div>
   </div>
 </div>

=======
  .axis--x path {
    display: none;
  }

  .line {
    fill: none;
    stroke: steelblue;
    stroke-width: 1.5px;
  }
</style>

<body>
  <svg width="1000" height="500"></svg>
  <div id="issue_list"></div>
>>>>>>> cf2458e (added a dropdown for relevance graph)
</body>

<!--Brian was Here-->


