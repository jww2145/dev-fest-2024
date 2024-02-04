/**
* While this component is not done yet, we have big plans!
* Unforunately, we did not have enough time in this hackathon
* to completely analyze all 435 house of representatives. 
* 
*
* @authors Joshua Wu
*/
<script>
    import HouseReps from "./House-Reps.svelte";
    import HouseCard from "./House-Card.svelte";
    let rep_data = null

    function handleSelectRep(event) {
        const repData = event.detail.rep;

        rep_data = repData['properties']

    }
</script>

<div class = 'container'>
    <div class = 'container-child-left'>
        <HouseReps on:selectRep={handleSelectRep}/>
    </div>
    <div class = 'container-child-right'>   
        <HouseCard rep = {rep_data}/>
    </div>
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

    .container-child-left{
        width: 60%;
        padding:1%;
        background-color: none;
        font-family: Georgia, 'Times New Roman', Times, serif;
        font-size:12pt;
        text-align:center;
        border: none;
    }

    .container-child-right{
        width: 27%;
        padding: 3%;
        background-color:none;
        font-family: Georgia, 'Times New Roman', Times, serif;
        font-size: 12pt;
        text-align: center;
        border: none;
    }
</style>