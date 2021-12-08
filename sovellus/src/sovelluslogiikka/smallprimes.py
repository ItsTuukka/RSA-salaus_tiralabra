class small_primes:
    
    """Luokka pienten alkulukujen luomiseen.

    Attributes: 
        up_till: Integer, mihin asti alkulukuja generoidaan.
        prime_list: Lista alkuluvuista. 
    """

    def __init__(self, up_till):
        """Luokan konstruktori.

        Args:
            up_till: Integer, mihin asti alkulukuja generoidaan.
        """

        self.up_till = up_till
        self.prime_list = self.generate_list(self.up_till)

    def generate_list(self, n):
        """Luo listan alkuluvuista lukuun n asti Eratostheneen seulalla.

        Args: 
            n: Integer, mihin asti alkulukuja luodaan.

        Returns: 
            Listan alkuluvuista.
        """

        primes = [True for i in range(n+1)]
        for i in range(2, n+1):
            if primes[i]:
                for j in range(i*i, n+1, i):
                    primes[j] = False
        prime_list = []
        for i in range(2, n+1):
            if primes[i]:
                prime_list.append(i)
        return prime_list