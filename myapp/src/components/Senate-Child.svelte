/**
* Our proudest achievement during the 2024 Devfest! This component
* is the parent div to both the beautifully rendered current senator
* as well as the 'Senate-Card' that lists out contact information in case 
* a consistuent want to get in contact
*
* @authors Joshua Wu and Brian Echavarria
* @see ./data-exploration/senatorRating.csv 
*/
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
        <p class = 'senator-intro'>The Senate: Everything You Need to Know</p><p class = 'senator-sub-intro'>Click a senator for more information!</p>
        <SenatorCard senator={senator_data} progress={progress}/>
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