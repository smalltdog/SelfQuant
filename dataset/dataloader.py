import dataloader

class DataLoader(dataloader.DataLoader):
    def __init__(self, dataset, batch_size=1, shuffle=False, num_workers=0):
        super(DataLoader, self).__init__(dataset, batch_size=batch_size, shuffle=shuffle, num_workers=num_workers)
    def __iter__(self):
        for batch in super(DataLoader, self).__iter__():
            yield batch