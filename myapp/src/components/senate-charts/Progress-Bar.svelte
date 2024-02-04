/**
* This component was made to display a senator's environmental score,
* which was obtained by scraping the https://scorecard.lcv.org/scorecard?year=2022
* website and aggregate the total pro-environmental votes and dividing it by
* the total number of votes
*
* @authors Joshua Wu
*/
<script>
    import Progress from "./Progress.svelte";
    export let progress = null;
</script>

<br>
<h1>Environmental Score</h1>
<Progress progress = {progress}/>
