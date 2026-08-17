import mosaik_api

META = {
    'models': {
        'Sender': {
            'public': True,
            'params': ['eid', 'location', 'period'],
            'attrs': ['v', 't'],
        },
    },
}

class SenderSim(mosaik_api.Simulator):
    def __init__(self):
        super().__init__(META)
        self.data = {}
        self.time = 0
        
    def init(self, sid, verbose=0):
        self.sid = sid
        self.verbose = verbose
        
        return self.meta
    
    def create(self, num, model, eid, location, period=1):
        self.interval = period
        self.eid = eid
        self.location = location
        if (self.verbose > 0): print('simulator_sender::create ', model, ": ", eid, " location: ", location, " interval: ", period)
        
        return [{'eid': eid, 'type': model}]

    def step(self, time, inputs):
        self.time = time
        if (self.verbose > 0): print('simulator_sender::step: ', time)
        if (self.verbose > 1): print('simulator_sender::step INPUT: ', inputs)

        if (time % self.interval == 0):
            self.data[time] = int(self.location)

        return self.time + 1

    def get_data(self, inputs):
        if (self.verbose > 0): print('simulator_sender::get_data INPUT ', inputs)

        output = {}
        # Formatting output from stored data
        if (self.time % self.interval == 0):
            output[self.eid] = {}
            output[self.eid]['v'] = []
            output[self.eid]['t'] = []
            output[self.eid]['v'].append(self.data[self.time])
            # Scheduling at a later time for NS-3
            output[self.eid]['t'].append(self.time + 1)
        else:
            output[self.eid] = {}
            output[self.eid]['v'] = []
            output[self.eid]['t'] = []
            output[self.eid]['v'].append(None)
            # Scheduling at a later time for NS-3
            output[self.eid]['t'].append(None)

        if (self.verbose > 0): print('simulator_sender::get_data OUTPUT ', output)

        return output