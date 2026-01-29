using System.Net.Http;
using System.Text;
using System.Text.Json;

class Program
{
    static async Task Main()
    {
        using HttpClient client = new HttpClient();

        var novoJogo = new Jogo
        {
            nome = "Celeste",
            genero = "Plataforma",
            ano = 2018
        };

        var json = JsonSerializer.Serialize(novoJogo);
        var content = new StringContent(json, Encoding.UTF8, "application/json");

        var response = await client.PostAsync(
            "http://127.0.0.1:8000/jogos",
            content
        );

        Console.WriteLine(response.IsSuccessStatusCode
            ? "✅ Jogo enviado para o backend!"
            : "❌ Erro ao enviar jogo");
    }
}
