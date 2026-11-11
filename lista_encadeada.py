
class No:
    def __init__(self, id, titulo, categoria, descricao, requisitos, local):
        self.id = id
        self.titulo = titulo
        self.categoria = categoria
        self.descricao = descricao
        self.requisitos = requisitos
        self.local = local
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    # Cadastrar um novo serviço
    def inserir(self, id, titulo, categoria, descricao, requisitos, local):
        if self.buscar_por_id(id) is not None:
            print("Já existe um serviço com esse ID.")
            return

        novo = No(id, titulo, categoria, descricao, requisitos, local)

        if self.inicio is None:
            self.inicio = novo
        else:
            atual = self.inicio

            while atual.proximo is not None:
                atual = atual.proximo

            atual.proximo = novo

    # Listar todos os serviços
    def listar(self):
        if self.inicio is None:
            print("Nenhum serviço cadastrado.")
            return

        atual = self.inicio

        while atual is not None:
            print("\n-----------------------------")
            print(f"ID: {atual.id}")
            print(f"Título: {atual.titulo}")
            print(f"Categoria: {atual.categoria}")
            print(f"Descrição: {atual.descricao}")
            print(f"Requisitos: {atual.requisitos}")
            print(f"Local: {atual.local}")

            atual = atual.proximo

    # Buscar um serviço pelo ID
    def buscar_por_id(self, id):
        atual = self.inicio

        while atual is not None:
            if atual.id == id:
                return atual

            atual = atual.proximo

        return None

    # Buscar serviços pela categoria
    def buscar_por_categoria(self, categoria):
        atual = self.inicio
        encontrou = False

        categoria = categoria.strip().lower()

        while atual is not None:
            if atual.categoria.strip().lower() == categoria:
                print(f"\nID: {atual.id}")
                print(f"Título: {atual.titulo}")
                print(f"Categoria: {atual.categoria}")
                encontrou = True

            atual = atual.proximo

        if not encontrou:
            print("Nenhum serviço encontrado nessa categoria.")

    # Atualizar informações de um serviço
    def atualizar(self, id, titulo, categoria, descricao, requisitos, local):
        atual = self.buscar_por_id(id)

        if atual is None:
            print("Serviço não encontrado.")
            return

        atual.titulo = titulo
        atual.categoria = categoria
        atual.descricao = descricao
        atual.requisitos = requisitos
        atual.local = local

        print("Serviço atualizado com sucesso!")

    # Excluir um serviço pelo ID
    def excluir(self, id):
        if self.inicio is None:
            print("A lista está vazia.")
            return

        if self.inicio.id == id:
            self.inicio = self.inicio.proximo
            print("Serviço excluído com sucesso!")
            return

        anterior = self.inicio
        atual = self.inicio.proximo

        while atual is not None:
            if atual.id == id:
                anterior.proximo = atual.proximo
                print("Serviço excluído com sucesso!")
                return

            anterior = atual
            atual = atual.proximo

        print("Serviço não encontrado.")

    # Exibir estatísticas dos serviços
    def analisar(self):
        if self.inicio is None:
            print("A lista está vazia.")
            return

        total = 0
        categorias = {}
        atual = self.inicio

        while atual is not None:
            total += 1
            categoria = atual.categoria

            if categoria in categorias:
                categorias[categoria] += 1
            else:
                categorias[categoria] = 1

            atual = atual.proximo

        print("\n===== ESTATÍSTICAS =====")
        print(f"Total de serviços: {total}")

        print("\nServiços por categoria:")
        for categoria, quantidade in categorias.items():
            print(f"{categoria}: {quantidade}")

    # Ordenar alfabeticamente usando Selection Sort
    def ordenar(self):
        if self.inicio is None:
            print("A lista está vazia.")
            return

        atual = self.inicio

        while atual is not None:
            menor = atual
            proximo = atual.proximo

            while proximo is not None:
                if proximo.titulo.lower() < menor.titulo.lower():
                    menor = proximo

                proximo = proximo.proximo

            if menor != atual:
                atual.id, menor.id = menor.id, atual.id
                atual.titulo, menor.titulo = menor.titulo, atual.titulo
                atual.categoria, menor.categoria = menor.categoria, atual.categoria
                atual.descricao, menor.descricao = menor.descricao, atual.descricao
                atual.requisitos, menor.requisitos = menor.requisitos, atual.requisitos
                atual.local, menor.local = menor.local, atual.local

            atual = atual.proximo

        print("Serviços ordenados com sucesso!")

    # Verificar se já existe um serviço com o mesmo título
    def buscar_por_titulo(self, titulo):
        atual = self.inicio

        while atual is not None:
            if atual.titulo.strip().lower() == titulo.strip().lower():
                return atual

            atual = atual.proximo

        return None
