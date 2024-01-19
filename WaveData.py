import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waveproc

class WaveData:
    def __init__(self, fname=''):
        self._validData = 0
        if (fname!=''):
            self._validData = self.ReadData(fname)
        #return self._validData

    def ReadData(self,fname):
        _success = 0
        if fname.lower().endswith(('.wav')):
            self._samplerate, self._data = waveproc.read(fname) #framerate
            self._n_channels = self._data.shape[1]
            self._time_length = self._data.shape[0] / self._samplerate
            self._n_samples = self._data.shape[0]
            if (self._n_channels>1):
                self._l_channel = self._data[:,0]
                self._r_channel = self._data[:,1]
            else:
                self._l_channel = self._data[:,0]
                self._r_channel = self._data[:,0]
            #wav_obj = wave.open(wav_fname, 'rb')
            #self._samplerate = wav_obj.getframerate()
            #self._n_samples = wav_obj.getnframes()
            #self._time_length = self._n_samples/self._samplerate 
            #self._n_channels = wav_obj.getnchannels()
            #signal_wave = wav_obj.readframes(n_samples)
            #ignal_array = np.frombuffer(signal_wave, dtype=np.int16)
            #self._l_channel = signal_array[0::2]
            #self._r_channel = signal_array[1::2]
            _success = 1
        return _success

    def PlotChannel(self,channel=0):
        if (self._validData!=0):
            times = np.linspace(0, self._n_samples/self._samplerate, num=self._n_samples)
            plt.figure(figsize=(15, 5))
            plt.plot(times, self._l_channel)
            plt.title('Left Channel')
            plt.ylabel('Signal Value')
            plt.xlabel('Time (s)')
            plt.xlim(0, self._time_length)
            plt.show()
        return self._validData

    def PlotSpectogram(self,channel=0):
        if (self._validData!=0):
            # frequency spectrum, also known as a spectrogram
            plt.figure(figsize=(15, 5))
            plt.specgram(self._l_channel, Fs=self._samplerate, vmin=-20, vmax=50)
            plt.title('Left Channel')
            plt.ylabel('Frequency (Hz)')
            plt.xlabel('Time (s)')
            plt.xlim(0, self._time_length)
            plt.colorbar()
            plt.show()
        return self._validData

    def __str__(self):
        return f"{self.name}({self.age})"    
        
#if __name__ == "__main__":
