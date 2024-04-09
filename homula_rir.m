% HOMULA-RIR sample code
% Author: Federico Miotello (federico.miotello@polimi.it)
% Date: April 9th, 2024

clear;
close all;
clc;

addpath(genpath('HOMULA-RIR')); % Path to dataset folder

%% Read a RIR

wav_file = 'hom/row3/rir-S1-R3-HOM2.wav';
[rir, fs] = audioread(wav_file); % Reading RIR between source S1 and HOM 2 in 3rd row

%% Plot a RIR

ch = 1; % Channel within the microphone array
samples_to_plot = 0.1*fs; % Plotting the first 0.1 secs

figure(1)
time_ax = 1/fs*(1:length(rir));
plot(time_ax(1:samples_to_plot), rir(1:samples_to_plot,ch));

%% Plot source and mic positions in 3D

sources_pos = table2array(readtable('pos-sources.csv'));
mic_pos = table2array(readtable('hom/row3/pos-R3-HOM2.csv'));

% Room dimensions
x_dim = [0 5.46];
y_dim = [0 14.52];
z_dim = [0 3.38];

figure(2)
hold on
axis equal

scatter3(mic_pos(:,1), mic_pos(:,2), mic_pos(:,3), 'blue')
scatter3(sources_pos(2,1), sources_pos(2,2), sources_pos(2,3), 'green')

hold off

xlim(x_dim);
ylim(y_dim);
zlim(z_dim);

get(gca);
set(gca,'XDir','reverse'); % Inverted axis to reproduce real room setup



