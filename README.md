# HOMULA-RIR: A Room Impulse Response Dataset for Teleconferencing and Spatial Audio Applications Acquired Through Higher-Order Microphones and Uniform Linear Microphone Arrays

HOMULA-RIR is a dataset of room impulse responses (RIRs) acquired using both higher-order microphones (HOMs) and a uniform linear array (ULA), in order to model a remote attendance teleconferencing scenario. Specifically, measurements were performed in a seminar room, where a 64-microphone ULA (*Eventide-Polimi eStick*) was used as a multichannel audio acquisition system in the proximity of 2 speakers (*Genelec 8020*), while HOMs (*Voyage Audio Spatial Mic*) were used to model 25 attendees actually present in the seminar room.

* [***Read the paper***](https://arxiv.org/abs/2402.13896) 📄
* [***Download the dataset***](https://zenodo.org/records/10479726) ⬇️

<br>

<img src="https://github.com/polimi-ispl/homula-rir/assets/17434626/79b44352-bf62-4b37-8c29-971ce1a13adc" alt="drawing" width="490"/>
<img src="https://github.com/polimi-ispl/homula-rir/assets/17434626/07640a94-bdf6-4fc2-bd51-4b1f3c18931e" alt="drawing" width="490"/>


<br>RIRs have been recorded at a sample rate of *fs = 48 kHz* and truncated to a duration of *1 s*. They are provided as multichannel `wav` files, saved at *32 bit* per sample.
Together with RIRs we also release acoustically calibrated positions of each microphone capsule.

## Naming convention

RIRs of individual arrays are saved as separate files, following the naming convention: <code>rir-**source**-**array**.wav</code>. Here, <code>**source**</code> can be either `S1` or `S2`, depending on the considered source, and array is an acronym representing a specific microphone array, as depicted in the previous picture. The term <code>**array**</code> can take on either `ULA` for the eSticks measures, or a pair <code>**row**-**HOM**</code> for the Spatial Mics measures. Specifically, <code>**row**</code> = {<code>R1</code>, <code>R2</code>, <code>R3</code>, <code>R4</code>, <code>R5</code>} designates the row where a particular Spatial Mic is positioned, and <code>**HOM**</code> = {<code>HOM1</code>, <code>HOM2</code>, <code>HOM3</code>, <code>HOM4</code>, <code>HOM5</code>} denotes a specific array within each row. The positions of each capsule in every array are released as `csv` files, adopting the naming convention <code>pos-**array**.csv</code>, where <code>**array**</code> is the same acronym denoting a specific microphone array. Additionally, the positions of the two sources are reported in the file `pos-sources.csv`.

## Authors

*[Federico Miotello](https://github.com/fmiotello)*<br>
*[Paolo Ostan](https://github.com/pos17)*<br>
*[Mirco Pezzoli](https://github.com/m-pexx)*<br>
*[Luca Comanducci](https://github.com/lucacoma)*<br>
*Alberto Bernardini*<br>
*Fabio Antonacci*<br>
*Augusto Sarti*<br>

