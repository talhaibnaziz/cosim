import mosaik_api

META = {
    'models': {
        'Receiver': {
            'public': True,
            'params': ['eid', 'location'],
            'attrs': ['v', 't'],
        },
    },
}

class ReceiverSim(mosaik_api.Simulator):
    def __init__(self):
        super().__init__(META)
        self.data = {}
        self.time = 0
        
    def init(self, sid, verbose=0):
        self.sid = sid
        self.verbose = verbose
        
        return self.meta
    
    def create(self, num, model, eid, location):
        if (self.verbose > 0): print('simulator_receiver::create ', model, " : ", eid, " location: ", location)
        
        return [{'eid': eid, 'type': model}]

    def step(self, time, inputs):
        self.time = time
        if (self.verbose > 0): print('simulator_receiver::step: ', time)
        if (self.verbose > 2): print('simulator_receiver::step INPUT: ', inputs)

        for receiver_eid, attrs in inputs.items():
            vlist = list(attrs['v'].values())[0]
            tlist = list(attrs['t'].values())[0]

            for i in range(0, len(vlist)):
                input_v = vlist[i]
                input_t = tlist[i]

                if (input_v != 'None' and self.verbose > 1):
                    print('simulator_receiver::received data from sender:')
                    print('message: ', input_v, ' time: ', self.time, ' total delay: ', self.time - int(input_t))

        return self.time + 1