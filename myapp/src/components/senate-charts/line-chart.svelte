<script>
  import { onMount } from "svelte";
  import * as d3 from "d3";

<<<<<<< HEAD
  export const prerender = true;

=======
  let svg;
  let issues;
  let x;
  let y;
  let myLine;
>>>>>>> 163169ea7b015f2db47506063e3268cc5ba1fb9d

  onMount(() => {
    const margin = { top: 20, right: 80, bottom: 30, left: 50 };
    const width = 1000 - margin.left - margin.right;
    const height = 500 - margin.top - margin.bottom;

    svg = d3.select("svg");

    const g = svg
      .append("g")
      .attr("transform", `translate(${margin.left},${margin.top})`);

    x = d3.scaleLinear().domain([1971, 2023]).range([0, width]);
    y = d3.scaleLinear().domain([1, 0]).range([height, 0]);

    myLine = g.append("path");

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

        g.append("g")
          .attr("class", "axis axis--y")
          .call(d3.axisLeft(y))
          .append("text")
          .attr("transform", "rotate(-90)")
          .attr("y", 6)
          .attr("dy", "0.71em")
          .attr("fill", "#000")
          .text("Count");

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
</body>

<!--Brian was Here-->


