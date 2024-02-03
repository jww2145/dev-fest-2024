// Define global variables
const senator_radius = 17;
const width = 800; // Define a suitable width for your visualization
let height = 600; // Initially define a suitable height, will be recalculated
const legendItems = ["Yes", "No", "Missing"];

const color = (d) => {
  if (d === "Yes") return "#50CDA4";
  if (d === "No") return "#e41a1c";
  return "#F3F3F3";
};

document.addEventListener('DOMContentLoaded', function() {
  
  //Math on how to handle row assignments
  const row_assignments = (() => {
    let arr = [];
    let r = 0;
    const row_max = [8, 9, 10, 11, 12];
    const row_count = [0, 0, 0, 0, 0];
    
    for (let i = 0; i < 50; i++) {
      while (row_count[r] === row_max[r]) r = (r + 1) % 5;
      row_count[r] += 1;
      arr[i] = r;
      r = (r + 1) % 5;
    }
    
    return arr;
  })();

  const row = (i) => {
    return row_assignments[i];
  };

  const senators_in_row = (i) => {
    return 8 + row(i);
  };

  const radius = (i) => row(i) * senator_radius * 3 + 200;

  const angle = (i) => {
    const position_in_row = (j) => {
      let pos = 0;
      for (let k = 50; k > j; k--) {
        if (row(k) === row(j)) pos++;
      }
      return pos;
    };
    return -(Math.PI / 2) * (position_in_row(i) / (senators_in_row(i) - 1));
  };

  const x = (i) => {
    const j = (i < 50 ? i : i - 50);
    const offset = Math.cos(angle(j)) * radius(j) + senator_radius * 3;
    return (width / 2) + (i < 50 ? offset : -offset);
  };

  const y = (i) => {
    const j = i < 50 ? i : i - 50;
    return (height - senator_radius - 2) + Math.sin(angle(j)) * radius(j);
  };

  // Recalculate height based on the layout
  height = radius(4) + senator_radius * 2 + 20;

  
  d3.json("https://theunitedstates.io/congress-legislators/legislators-current.json").then(data => {
    const senators = data.map(({name, id, terms}) => ({
        name,
        bioguide: id.bioguide,
        ...terms[terms.length - 1]
    })).filter((d) => d.type === "sen").sort((a, b) => {
        return a.party < b.party ? -1 : 1;
    }).reverse();

    // Create the SVG element after loading the data
    const svg = d3.select('body').append('svg')
                    .attr("width", width)
                    .attr("height", height);

    // Clip Path for senator images
    svg.append("defs")
      .append("clipPath")
      .attr("id", "clip-circle")
      .append("circle")
      .attr("cx", senator_radius)
      .attr("cy", senator_radius)
      .attr("r", senator_radius);

    // Bind senator data to create senator elements
    const sens = svg.selectAll("g.senator")
      .data(senators)
      .enter()
      .append('g')
      .attr('class', 'senator')
      .attr("transform", (d, i) => `translate(${x(i)}, ${y(i)})`);

    // Append circles for senators
    sens.append("circle")
      .attr("r", senator_radius + 2)
      .attr("cx", 0)
      .attr("cy", 0)
      .attr("fill", (d) => color(d.party))
      .append("title").text((d) => d.name.official_full);

    sens.append("circle")
      .attr("r", senator_radius + 1)
      .attr("cx", 0)
      .attr("cy", 0)
      .attr("fill", "rgba(255, 255, 255, 0.8)")
      .append("title").text((d) => d.name.official_full);

    // Append images if enabled
    if (images === "true") {
      sens.append('image')
        .attr('xlink:href', (d) => `https://theunitedstates.io/images/congress/225x275/${d.bioguide}.jpg`)
        .attr('width', senator_radius * 2)
        .attr('height', senator_radius * 2) // Added height to ensure the image appears correctly
        .attr('x', -senator_radius)
        .attr('y', -senator_radius)
        .attr('clip-path', 'url(#clip-circle)');
    }

    // Create legend
    const legend = svg.append('g')
      .attr("transform", `translate(${width - 125}, 20)`)
      .selectAll('g.legend')
      .data(legendItems)
      .enter()
      .append('g')
      .attr('class', 'legend')
      .attr('transform', (d, i) => `translate(0, ${i * 25})`);

    legend.append('rect')
      .attr('x', 0)
      .attr('y', -5)
      .attr('width', 10)
      .attr('height', 10)
      .attr('fill', color);

    legend.append('text')
      .attr('x', 15)
      .attr('y', 5)
      .text((d) => d);
  });
});
