<script>
    import { onMount, createEventDispatcher } from 'svelte';
    import * as d3 from 'd3';
    import { feature } from 'topojson-client';

    export const prerender = true;


    const hasNoCongressionalRep = ['Puerto Rico', 'District of Columbia', 'U.S. Virgin Islands', 'Guam', 'Northern Mariana Islands', 'American Samoa']
    const dispatch = createEventDispatcher();
    const usAbbrs = {
        AL: 'Alabama',
        AK: 'Alaska',
        AS: 'American Samoa',
        AZ: 'Arizona',
        AR: 'Arkansas',
        CA: 'California',
        CO: 'Colorado',
        CT: 'Connecticut',
        DE: 'Delaware',
        DC: 'District Of Columbia',
        FM: 'Federated States Of Micronesia',
        FL: 'Florida',
        GA: 'Georgia',
        GU: 'Guam',
        HI: 'Hawaii',
        ID: 'Idaho',
        IL: 'Illinois',
        IN: 'Indiana',
        IA: 'Iowa',
        KS: 'Kansas',
        KY: 'Kentucky',
        LA: 'Louisiana',
        ME: 'Maine',
        MH: 'Marshall Islands',
        MD: 'Maryland',
        MA: 'Massachusetts',
        MI: 'Michigan',
        MN: 'Minnesota',
        MS: 'Mississippi',
        MO: 'Missouri',
        MT: 'Montana',
        NE: 'Nebraska',
        NV: 'Nevada',
        NH: 'New Hampshire',
        NJ: 'New Jersey',
        NM: 'New Mexico',
        NY: 'New York',
        NC: 'North Carolina',
        ND: 'North Dakota',
        MP: 'Northern Mariana Islands',
        OH: 'Ohio',
        OK: 'Oklahoma',
        OR: 'Oregon',
        PW: 'Palau',
        PA: 'Pennsylvania',
        PR: 'Puerto Rico',
        RI: 'Rhode Island',
        SC: 'South Carolina',
        SD: 'South Dakota',
        TN: 'Tennessee',
        TX: 'Texas',
        UT: 'Utah',
        VT: 'Vermont',
        VI: 'Virgin Islands',
        VA: 'Virginia',
        WA: 'Washington',
        WV: 'West Virginia',
        WI: 'Wisconsin',
        WY: 'Wyoming',
    }

    onMount(() => {
      
      fetchCongress().then(buildMap)

      function fetchCongress(){
          return d3.json('https://gist.githubusercontent.com/jeremiak/3bd59f8f0ac405a423f2f66f516f43aa/raw/0888caf3eb6731fa7defdedd1f784401c0e320b6/us-congress.json').then(response => buildCongress(response))
      }

      function buildCongress(topo){
          let geojson = feature(topo, topo.objects.us_congress)
          geojson = geojson.features.filter(f => !hasNoCongressionalRep.includes(f.properties.STATE))
          return geojson;
      }

      function buildMap(geojsonData) {
          const svg = d3.select("#map");
          const width = 960;
          const height = 600;

          const projection = d3.geoAlbersUsa().translate([width / 2, height / 2]).scale(1000);
          const path = d3.geoPath().projection(projection);

          svg.selectAll("path")
              .data(geojsonData)
              .enter()
              .append("path")
              .attr("d", path)
              .style("fill", "steelblue")
              .on('click', function(event, d){
            
                const sel = d3.select(this); 
                dispatch('selectRep', { rep: d });
                const currentFill = sel.style('fill');
                const nextFill = currentFill !== 'rgb(238, 173, 117)' ? 'rgb(238, 173, 117)' : 'steelblue';
                sel.style('fill', nextFill);
            });

      }

  });
  </script>
  
  <svg id="map" width="960" height="600"></svg>

  