<script>
    import Senators from "./Senators.svelte";
    import SenatorCard from "./Senator-Card.svelte";
    import Papa from 'papaparse';

    export const prerender = true;


    let senator_data = null
    let progress = null
    function handleSelectSenator(event) {
        const senatorData = event.detail.senator;

        senator_data = senatorData

        let last = senatorData['name']['last']

        const response = fetch('https://gist.githubusercontent.com/jww2145/d4aed4da427841e080f2e05f4bdcc271/raw/a4444c6c7246a9bd924b9650ec65191da4992a69/ratings.csv')
            .then(response => response.text())
            .then(v => Papa.parse(v))
            .catch(err => console.log(err))
        response.then(v => findSenator(v,last))
        
        // Now you can use senatorData as needed, e.g., pass it to another component or use it in this component
    }

    function findSenator(arr,name){
  
        let array1 = arr['data']

        array1.forEach(element => {
            if (name == element[0].split(',')[0]){
                progress = element[3]
            }
        })
        
    }
</script>

<div class = 'container'>
    <div class = 'container-child-left'>
<<<<<<< HEAD
        <p class = 'senator-intro'>The Senate: Everything You Need to Know</p><p class = 'senator-sub-intro'>Click a senator for more information!</p>
        <SenatorCard senator={senator_data} progress={progress}/>
=======
        <p class = 'senator-intro'>Les sénateurs: everything you need to know</p><p class = 'senator-sub-intro'>Hover over a senator for more information!</p>
        <p>
            Hello! 8=>

            Donec rhoncus ut tellus in suscipit. Proin rutrum sit amet elit eu ornare.
            Donec sed mi gravida, scelerisque dolor sit amet, ornare felis. Fusce vestibulum, 
            ipsum nec aliquam dictum, purus ante facilisis odio, ut tincidunt erat dui nec sem. Morbi eu libero mollis, 
            porttitor felis et, pulvinar odio. Suspendisse eget nibh vitae purus maximus congue ac eu eros. Vestibulum quis 
            massa vitae lacus molestie pretium. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac 
            turpis egestas. Vestibulum eu diam nec ex aliquet pulvinar. Sed ac condimentum metus, in vulputate purus. Nunc in
            metus mollis leo tempus luctus. Curabitur consectetur aliquam elit. Maecenas non ullamcorper neque.
          </p>
>>>>>>> cf2458e (added a dropdown for relevance graph)
    </div>
    <div class = 'container-child-right'><Senators on:selectSenator={handleSelectSenator}/></div>
</div>

<style>

.container{
        display:flex;
        flex-direction: row;
        flex-wrap: nowrap;
        justify-content: space-around;
        align-items: center;
        align-content: center;
    }

    .senator-intro{
        font-size: large;
        font-family: Georgia, 'Times New Roman', Times, serif;
        font-weight: bolder;
    }
    .senator-sub-intro{
        font-family: 'Courier New', Courier, monospace;
        font-size: smaller;
        margin-top:-3%;
    }
    .container-child-left{
        width: 27%;
        padding:3%;
        background-color: none;
        font-family: Georgia, 'Times New Roman', Times, serif;
        font-size:12pt;
        text-align:left;
        border: none;
    }

    .container-child-right{
        width: 60%;
        padding: 1%;
        background-color:none;
        font-family: Georgia, 'Times New Roman', Times, serif;
        font-size: 12pt;
        border: none;
    }

    p{
        line-height: 130%;
    }
</style>