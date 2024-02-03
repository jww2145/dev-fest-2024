<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';

    const senator_radius = 17;
    const width = 1000; // Define a suitable width for your visualization
    const height = 450; // Initially define a suitable height, will be recalculated
    let container;
    const color = (d) => {
        if(d == "Democrat") return "#377eb8";
        if(d == "Republican") return "#e41a1c";
        return "#4daf4a";
    }

    let senators = []; // Placeholder for senator data
    let images = "true"; // or false, depending on your needs
    const legendItems = ["Democrat", "Republican", "Independent"]

    let row = (i) => {
        return row_assignments[i];
    }

    let position_in_row = (i) => {
        let pos = 0;
        for(let j = 50; j > i; j--) {
            if(row(j) == row(i)) pos++;
        }
        return pos;
    }

    let senators_in_row = (i) => {
        return 8 + row(i);
    }

    let radius = (i) => row(i) * senator_radius * 3 + 200

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

    const angle = (i) => {
        return -(Math.PI / 2) * (position_in_row(i) / (senators_in_row(i) - 1))
    }

    const x = (i) => {
        const j = (i < 50 ? i : i - 50);
        const offset = Math.cos(angle(j)) * radius(j) + senator_radius*3;
        return (width / 2) + (i < 50 ? offset : -offset);
    }

    const y = (i) => {
        const j = i < 50 ? i : i - 50;
        return (height - senator_radius - 2) + Math.sin(angle(j)) * radius(j);
    }

    onMount(() => {
        fetchSenators().then(data => {
            senators = data;
            buildChart(); // Ensure chart is built after data is fetched and processed
        });
    });

    function fetchSenators() {
        return d3.json("https://theunitedstates.io/congress-legislators/legislators-current.json")
        .then(response => response
            .map(({name, id, terms}) => ({
            name, 
            bioguide: id.bioguide, 
            ...terms[terms.length - 1]
            }))
            .filter(d => d.type === "sen")
            .sort((a, b) => b.party.localeCompare(a.party)) // Sort senators by party
        );
  }


    function buildChart() {
        const svg = d3.select(container)
        .append("svg")
        .attr("width", width)
        .attr("height", height);

        svg.append("defs")
            .append("clipPath")
            .attr("id", "clip-circle")
            .append("circle")
            .attr("cx", senator_radius)
            .attr("cy", senator_radius)
            .attr("r", senator_radius);

        const sens = svg.selectAll("g.senator")
            .data(senators)
            .enter()
            .append('g')
            .attr('class', 'senator')
            .attr("transform", (d, i) => `translate(${x(i)}, ${y(i)})`);

        sens
            .append("circle")
            .attr("r", senator_radius + 2)
            .attr("cx", 0)
            .attr("cy", 0)
            .attr("fill", (d) => color(d.party))
            .append("title").text((d) => d.name.official_full);

        sens
            .append("circle")
            .attr("r", senator_radius + 1)
            .attr("cx", 0)
            .attr("cy", 0)
            .attr("fill", "rgba(255, 255, 255, 0.8)")
            .append("title").text((d) => d.name.official_full);

        if(images === "true") {
            sens
            .append('g')
            .attr('clip-path', 'url(#clip-circle)')
            .attr("transform", `translate(${-senator_radius}, ${-senator_radius})`)
            .append('image')
            .attr('href', (d) => `https://raw.githubusercontent.com/jww2145/images/gh-pages/congress/225x275/${d.bioguide}.jpg`) // Note: 'xlink:href' is now simply 'href'
            .attr('width', senator_radius * 2)
            .append("title").text((d) => d.name.official_full);
        }
    }

  </script>

  <div bind:this={container}></div>

  <style>
    div {
    width: 100%; /* Full width of its parent container */
    display: flex;
    justify-content: center;
    align-items: center;
    }
  </style>