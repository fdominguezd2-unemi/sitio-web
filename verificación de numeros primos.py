{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Welcome To Colaboratory",
      "provenance": [],
      "toc_visible": true,
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/fdominguezd2-unemi/sitio-web/blob/main/verificaci%C3%B3n%20de%20numeros%20primos.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "43cf9898"
      },
      "source": [
        "class Estudiante:\n",
        "    def __init__(self, cedula, nombres, apellidos, asignatura):\n",
        "        self.cedula = cedula\n",
        "        self.nombres = nombres\n",
        "        self.apellidos = apellidos\n",
        "        self.asignatura = asignatura\n",
        "        self.notas = []\n",
        "        self.promedio = 0.0\n",
        "        self.estado = \"\"\n",
        "\n",
        "    def capturar_notas(self):\n",
        "        while True:\n",
        "            try:\n",
        "                cantidad = int(input(f\"Ingrese la cantidad de notas para {self.nombres} (mínimo 4): \"))\n",
        "                if cantidad > 3:\n",
        "                    break\n",
        "                else:\n",
        "                    print(\"¡ALERTA! La cantidad de notas debe ser mayor a 3.\")\n",
        "            except ValueError:\n",
        "                print(\"Error: Ingrese un número entero válido.\")\n",
        "\n",
        "        for i in range(cantidad):\n",
        "            while True:\n",
        "                try:\n",
        "                    nota = float(input(f\"  Ingrese la nota {i+1} (0-100): \"))\n",
        "                    if 0 <= nota <= 100:\n",
        "                        self.notas.append(nota)\n",
        "                        break\n",
        "                    else:\n",
        "                        print(\"  La nota debe estar entre 0 y 100.\")\n",
        "                except ValueError:\n",
        "                    print(\"  Error: Ingrese un valor numérico.\")\n",
        "\n",
        "        self.calcular_promedio()\n",
        "\n",
        "    def calcular_promedio(self):\n",
        "        if self.notas:\n",
        "            self.promedio = sum(self.notas) / len(self.notas)\n",
        "            if 69.50 <= self.promedio <= 100:\n",
        "                self.estado = \"Aprobado\"\n",
        "            elif 39.50 <= self.promedio < 69.50:\n",
        "                self.estado = \"Suspenso\"\n",
        "            else:\n",
        "                self.estado = \"Reprobado\"\n",
        "\n",
        "    def __str__(self):\n",
        "        return f\"ID: {self.cedula} | {self.nombres} {self.apellidos} | Asig: {self.asignatura} | Promedio: {self.promedio:.2f} | Estado: {self.estado}\""
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 425
        },
        "id": "cd8465fe",
        "outputId": "57693dbe-156f-486e-c358-7103f191fcef"
      },
      "source": [
        "def menu():\n",
        "    lista_estudiantes = []\n",
        "    while True:\n",
        "        print(\"\\n--- MENÚ DE OPCIONES ---\")\n",
        "        print(\"1. Registrar estudiantes\")\n",
        "        print(\"2. Consultar promedios y estados del estudiante\")\n",
        "        print(\"3. Salir\")\n",
        "\n",
        "        opcion = input(\"Seleccione una opción: \")\n",
        "\n",
        "        if opcion == '1':\n",
        "            cedula = input(\"Cédula: \")\n",
        "            nombres = input(\"Nombres: \")\n",
        "            apellidos = input(\"Apellidos: \")\n",
        "            asignatura = input(\"Asignatura: \")\n",
        "\n",
        "            nuevo_estudiante = Estudiante(cedula, nombres, apellidos, asignatura)\n",
        "            nuevo_estudiante.capturar_notas()\n",
        "            lista_estudiantes.append(nuevo_estudiante)\n",
        "            print(\"Estudiante registrado con éxito.\")\n",
        "\n",
        "        elif opcion == '2':\n",
        "            if not lista_estudiantes:\n",
        "                print(\"No hay estudiantes registrados.\")\n",
        "            else:\n",
        "                print(\"\\n--- LISTA DE ESTUDIANTES ---\")\n",
        "                for est in lista_estudiantes:\n",
        "                    print(est)\n",
        "\n",
        "        elif opcion == '3':\n",
        "            print(\"Saliendo del programa...\")\n",
        "            break\n",
        "        else:\n",
        "            print(\"Opción no válida. Intente de nuevo.\")\n",
        "\n",
        "# Ejecutar el menú\n",
        "menu()"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "--- MENÚ DE OPCIONES ---\n",
            "1. Registrar estudiantes\n",
            "2. Consultar promedios y estados del estudiante\n",
            "3. Salir\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "Interrupted by user",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipykernel_14913/3055582019.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     35\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     36\u001b[0m \u001b[0;31m# Ejecutar el menú\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 37\u001b[0;31m \u001b[0mmenu\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/tmp/ipykernel_14913/3055582019.py\u001b[0m in \u001b[0;36mmenu\u001b[0;34m()\u001b[0m\n\u001b[1;32m      7\u001b[0m         \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"3. Salir\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 9\u001b[0;31m         \u001b[0mopcion\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Seleccione una opción: \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     10\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     11\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mopcion\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m'1'\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m   1175\u001b[0m                 \u001b[0;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1176\u001b[0m             )\n\u001b[0;32m-> 1177\u001b[0;31m         return self._input_request(\n\u001b[0m\u001b[1;32m   1178\u001b[0m             \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mprompt\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1179\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"shell\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m   1217\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1218\u001b[0m                 \u001b[0;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1219\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Interrupted by user\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1220\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1221\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Invalid Message:\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
          ]
        }
      ]
    }
  ]
}